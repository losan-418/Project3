from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from employee.models import UserModel,User
from django.contrib.auth.models import User
from employee.forms import UserForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"index.html")
def emp_add(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            u = user_form.save()
            message="Successfully saved."

            return redirect('emp_add',{'messages':message})
        else:
            messages.error(request,"Please fill the data correctly")
    else:
        user_form = UserForm()
        return redirect('emp_add', user_form)
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return redirect(request.GET['next'])
            return redirect('emp_list')
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "index.html", context)
    else:
        return render(request, "index.html", context)
def emp_list(request):
    # print(request.role)
    list_user = User.objects.all()
    return render(request, 'details.html', {'data':list_user})