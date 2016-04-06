from django.shortcuts import render, redirect, get_object_or_404

from .models import RecruitmentPeriod, RecruitableRole, RecruitmentApplication, RoleApplication
from django.forms import ModelForm
from django import forms

from django.forms import inlineformset_factory

class RecruitmentPeriodForm(ModelForm):
    class Meta:
        model = RecruitmentPeriod
        fields = '__all__'

        widgets = {
            "start_date": forms.TextInput(attrs={'class': 'datepicker'}),
            "end_date": forms.TextInput(attrs={'class': 'datepicker'}),
        }

class RecruitmentApplicationForm(ModelForm):
    class Meta:
        model = RecruitmentApplication
        fields = '__all__'

class RoleApplicationForm(ModelForm):

    def __init__(self, recruitment_period,*args,**kwargs):
        super (RoleApplicationForm,self ).__init__(*args,**kwargs)
        self.fields['recruitableRole'].queryset = RecruitableRole.objects.filter(recruitment_period=recruitment_period)


    class Meta:
        model = RoleApplication
        fields = ('recruitableRole',)

def recruitment(request, template_name='recruitment/recruitment.html'):
    recruitmentPeriods = RecruitmentPeriod.objects.all()
    data = {}
    data['recruitment_periods'] = recruitmentPeriods
    return render(request, template_name, data)

def recruitment_period(request, pk, template_name='recruitment/recruitment_period_new.html'):
    print(pk)
    return render(request, template_name, {})

def recruitment_period_new(request, template_name='recruitment/recruitment_period_new.html'):
    print("EY YO!")
    form = RecruitmentPeriodForm(request.POST or None)
    roles_form = inlineformset_factory(RecruitmentPeriod, RecruitableRole, fields=('role',))(request.POST or None)
    if form.is_valid() and roles_form.is_valid():
        recruitmentPeriod = form.save()
        roles_form.instance = recruitmentPeriod
        roles_form.save()
        return redirect('recruitment')
    else:
        print(form.errors)
        print("Ai'nt no valid form!")
    return render(request, template_name, {'form': form, 'roles_form': roles_form})

def recruitment_application_new(request, pk, template_name='recruitment/recruitment_application_new.html'):
    print("EY YO!")
    recruitment_period = get_object_or_404(RecruitmentPeriod, pk=pk)
    form = [RoleApplicationForm(recruitment_period, request.POST or None) for x in range(0, 1)]
    #form.instance = recruitment_period
    #roles_form = inlineformset_factory(RecruitmentApplication, RoleApplication, fields=('recruitmentApplication',))(request.POST or None)
    if all([form.is_valid() for form in form]):
        print("IT SORTA WORKED!")
        recruitment_application = RecruitmentApplication()
        recruitment_application.user = request.user
        recruitment_application.recruitmentPeriod = recruitment_period
        recruitment_application.save()
        for form in form:
            role = form.save(commit=False)
            role.recruitmentApplication = recruitment_application
            role.save()
        return redirect('recruitment')
    else:
        for form in form:
            print(form.errors)
        print("Ai'nt no valid form!")
    return render(request, template_name, {'form': form})


#delete a company
def recruitment_application_delete(request, pk):
    recruitmentApplication = get_object_or_404(RecruitmentApplication, pk=pk)
    recruitmentApplication.delete()
    return redirect('recruitment') #redirect back to company list