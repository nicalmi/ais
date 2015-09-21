from django.shortcuts import render
    
# Create your views here.

def list_people(request):
    if request.user.is_authenticated():
        username = request.user.username
        return render(request, 'people.html')
    return render(request, 'login.html')
    
