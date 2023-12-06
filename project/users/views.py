from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate
from users.forms import userCreationForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': userCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = userCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            thisUser = authenticate(username=username, password=password)
            login(request, thisUser)
            return redirect('home')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

