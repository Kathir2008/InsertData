from django.shortcuts import redirect, render
from InsertApp.models import login
# Create your views here.
def details(request):
    if request.method == 'POST' :
        user_name = request.POST.get('name_data')
        print(user_name)
        user_age = request.POST.get('age_data')
        print(user_name)
        user_mail = request.POST.get('mail_data')
        print(user_mail)
        user_password = request.POST.get('password_data')
        print(user_password)

        data = login(
            Name = user_name,
            age = user_age,
            Email = user_mail,
            Password = user_password
        )
        data.save()
        return redirect('base')
    return render(request , 'index.html')