from django.shortcuts import redirect, render
from appdata.models import value
# Create your views here.
def insert(request):
    if request.method == 'POST' :
        mail = request.POST.get('mail_id')
        password = request.POST.get('pass_id')
        DB = value(
            Email = mail,
            Password = password
        )
        DB.save()
        return redirect('get')
    return render(request , 'detalis.html')
def get(request):
    var = value.objects.all()
    dictionary = {'data' : var}
    return render(request , 'detalis.html' , context=dictionary)