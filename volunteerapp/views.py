from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import UserForm
from .models import UserProfile, Project, Tag
from .search import get_query


def Leaderboard(request):
    users = User.objects.all()[:5]
    context = {"users":users}
    return render(request, 'volunteerapp/leaderboard.html', context)

def ProjectDetail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {"project":project}
    return render(request, 'volunteerapp/project_detail.html', context)


def Index(request):
    projects = []
    query_string = ''
    selected_tag = ''
    tags = Tag.objects.all()
    project_set = Project.objects
    if ('tag' in request.GET) and request.GET['tag']:
        try:
            selected_tag = int(request.GET['tag'])
            project_set = Tag.objects.get(id=selected_tag).project_set
        except ValueError as e:
            pass
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        search_query = get_query(query_string, ['title', 'description'])
        project_set = project_set.filter(search_query).order_by('-created_at')
    projects = project_set.all()
    context = {"projects": projects, "query_string": query_string, "tags": tags, "selected_tag": selected_tag}
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
