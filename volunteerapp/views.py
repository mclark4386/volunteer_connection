from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from .models import UserProfile, Project
from .search import get_query


def Index(request):
    projects = []
    query_string = ''
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        search_query = get_query(query_string, ['title', 'description'])
        projects = Project.objects.filter(search_query).order_by('-created_at')
    else:
        projects = Project.objects.all()
    context = {"projects": projects, "query_string": query_string}
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
