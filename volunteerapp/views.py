from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from .models import UserProfile, Project


def Index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'volunteerapp/index.html', context)


class UserFormView(View):
    form_class = UserForm
    template_name = 'volunteerapp/registration_form.html'

    # display empty form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form post
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # any custom validation or cleaning
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            if len(password) < 8:  # if password is shorter than 8 chars
                return redirect(self)
            user.save()
            if user.profile is None:
                user.profile = UserProfile()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('volunteerapp:index')

        return render(request, self.template_name, {'form': form})
