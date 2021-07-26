from os import replace
from django.shortcuts import render
from demoallapp.models import detail
# Create your views here.
def play(request):
    if request.method == 'POST' :
        get_name = request.POST.get('name_id')
        get_age = request.POST.get('age_id')
        get_email = request.POST.get('email_id')
        get_pass = request.POST.get('pass_id')
    
        replay = detail(
            Name = get_name ,
            Age = get_age ,
            Email = get_email,
            password = get_pass
        )
        replay.save()
    return render(request , 'index.html')