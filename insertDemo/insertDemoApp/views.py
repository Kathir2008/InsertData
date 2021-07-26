from django.shortcuts import redirect, render
from insertDemoApp.models import data
# Create your views here.
def details(request):
    if request.method == 'POST' :
        email = request.POST.get('email_data')
        print(email)
        password = request.POST.get('password_data')
        print(password)
        MB = data(
            Email = email,
            Password = password
        )
        MB.save()

        return redirect ('value')
    return render(request , 'insert.html')