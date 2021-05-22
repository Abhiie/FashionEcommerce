from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf


# Create your views here.
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loginmodule/loggedin/')
    else:
        return HttpResponseRedirect('/loginmodule/invalidlogin/')


def loggedin(request):
    #return render(, )
    return render(request, 'loggedin.html', {"full_name":request.user.username})


def invalidlogin(request):

    return render(request, "invalidlogin.html")


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')
