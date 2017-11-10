from django.contrib import admin
from .models import ProjectCategory, Tag, Project, Participation, ProjectEmail


admin.site.register(ProjectCategory)
admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Participation)
admin.site.register(ProjectEmail)
