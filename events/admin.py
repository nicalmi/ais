import csv
from django.contrib import messages
from django.contrib import admin
from .models import Event, EventAttendence, EventQuestion, EventAnswer
from django.http import HttpResponse

# Exports all the EventAnswers that belong to a single Event
# (Could be expanded to include User information)
def export_as_csv(modeladmin, request, queryset):
    if len(queryset) != 1:
        modeladmin.message_user(request, 
            "Please select a single event to export", level=messages.ERROR)
        return

    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=event.csv'

    # We have already checked that it is a single event    
    event_id = queryset.first().id
    csv_headers = ['First name (user)', 'Last name (user)', 'Email (user)']
    question_list = []
    for question in EventQuestion.objects.filter(event__id = event_id):
        question_list.append(question.id)
        csv_headers.append(question.question_text)

    writer = csv.writer(response, quoting=csv.QUOTE_ALL)
    writer.writerow(csv_headers)
    for attendence in EventAttendence.objects.filter(event__id = event_id):
        user = attendence.user
        if user == None:
            user_information = [None, None, None]
        else:
            user_information = [
                attendence.user.first_name,
                attendence.user.last_name,
                attendence.user.email,
            ]
        answers = []
        # This requires an answer to all questions, atleast a null answer.
        for question in question_list:
            answers.append(EventAnswer.objects
                           .filter(question__id =  question)
                           .filter(attendence__id = attendence.id)
                           .first().answer)
        writer.writerow(user_information + answers)
    return response

class QuestionInline(admin.StackedInline):
    model = EventQuestion
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    filter_horizontal = ("allowed_groups",)
    actions = [export_as_csv]


class AnswerInline(admin.StackedInline):
    model = EventAnswer


class EventAttendenceAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Event, EventAdmin)

admin.site.register(EventAttendence, EventAttendenceAdmin)
