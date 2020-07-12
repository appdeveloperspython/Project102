from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def admin_login(request):
    return render(request,"admin_login.html")


def admin_welcome(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")
    
    if un == "aniket" and pa == "aniket":
        return render(request, "admin_welcome.html")
    else:
        messages.error(request,"Invalid Username & Password")
        return redirect('admin_login')

