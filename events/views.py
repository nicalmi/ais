import json

import stripe
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Count
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST

from events import serializers
from events.forms import EventForm, TeamForm
from events.models import Event, Team, Participant, SignupQuestion
from fair.models import Fair


def save_questions(questions_data, event):
    questions = []

    for question in questions_data:
        pk = question.pop('id', None)

        defaults = {
            'event': event,
            'type': question['type'],
            'question': question['question'],
            'required': question['required'],
            'options': question['options'],
        }

        q, _created = SignupQuestion.objects.update_or_create(pk=pk, defaults=defaults)
        questions.append(q)

    # This should work to override the questions with only the once that were sent, but it doesn't.
    event.signupquestion_set.set(questions)


@permission_required('events.base')
def event_list(request, year):
    fair = get_object_or_404(Fair, year=year)
    events = Event.objects.annotate(num_participants=Count('participant'))

    return render(request, 'events/event_list.html', {
        'fair': fair,
        'events': events
    })


@permission_required('events.base')
def event_new(request, year):
    fair = get_object_or_404(Fair, year=year)

    react_props = {
        'question_types': dict(SignupQuestion.QUESTION_TYPES)
    }

    form = EventForm(request.POST or None)

    if request.POST and form.is_valid():
        event = form.save()
        questions_data = json.loads(request.POST['questions'])

        save_questions(questions_data, event)
        return HttpResponse(status=200)

    return render(request, 'events/event_new.html', {
        'fair': fair,
        'form': form,
        'react_props': react_props
    })


@permission_required('event.base')
def event_edit(request, year, pk):
    fair = get_object_or_404(Fair, year=year)
    event = get_object_or_404(Event, pk=pk)

    react_props = {
        'questions': [serializers.signup_question(question) for question in event.signupquestion_set.all()],
        'question_types': dict(SignupQuestion.QUESTION_TYPES)
    }

    form = EventForm(request.POST or None, instance=event)

    if request.POST and form.is_valid():
        form.save()

        questions_data = json.loads(request.POST['questions'])

        save_questions(questions_data, event)
        return HttpResponse(status=204)

    return render(request, 'events/event_edit.html', {
        'fair': fair,
        'event': event,
        'form': form,
        'react_props': json.dumps(react_props)
    })


@login_required
def event_signup(request, year, event_pk):
    fair = get_object_or_404(Fair, year=year)
    event = get_object_or_404(Event, pk=event_pk)

    if not event.published:
        raise Http404

    payment_url = reverse('events:stripe_endpoint', args=[year, event_pk])

    react_props = {
        'event': serializers.event(event, request)
    }

    # Will be populated if user has started signup before
    participant = Participant.objects.filter(user_s=request.user).first()

    return render(request, 'events/event_signup.html', {
        'fair': fair,
        'event': event,
        'payment_url': payment_url,
        'participant': participant,
        'react_props': json.dumps(react_props)
    })


@require_POST
def stripe_endpoint(request, year, event_pk):
    event = get_object_or_404(Event, pk=event_pk)

    participant, _created = Participant.objects.get_or_create(
        user_s=request.user,
        event=event
    )

    if participant.fee_payed_s:
        return HttpResponseBadRequest('Fee has already been paid.')

    # Stripe expects the amount in ören
    amount = event.fee_s * 100
    token = request.POST['stripeToken']

    stripe.api_key = "sk_test_l4sPsGIoc2f8sD5N4D2fZkBY"
    charge = stripe.Charge.create(
        amount=amount,
        currency='sek',
        description=event.name,
        source=token
    )

    participant.stripe_charge_id = charge['id']
    participant.fee_payed_s = True
    participant.save()

    return HttpResponse(status=204)


@permission_required('event.base')
def team_edit(request, year, event_pk, team_pk):
    fair = get_object_or_404(Fair, year=year)
    event = get_object_or_404(Event, pk=event_pk)
    team = get_object_or_404(Team, pk=team_pk)

    form = TeamForm(request.POST or None, instance=team)

    if request.POST and form.is_valid():
        form.save()
        return redirect('events:event_edit', fair.year, event.id)

    return render(request, 'events/team_edit.html', {
        'fair': fair,
        'team': team,
        'form': form
    })


@permission_required('event.base')
def team_new(request, year, event_pk):
    fair = get_object_or_404(Fair, year=year)
    event = get_object_or_404(Event, pk=event_pk)

    form = TeamForm(request.POST or None, initial={'max_capacity': event.teams_default_max_capacity})

    if request.POST and form.is_valid():
        # We want to add the event_id here before saving the team
        new_team = form.save(commit=False)
        new_team.event = event
        new_team.save()
        return redirect('events:event_edit', fair.year, event.id)

    return render(request, 'events/team_edit.html', {
        'fair': fair,
        'form': form
    })
