from django.urls import path
from . import views
from.views import guide_login
urlpatterns = [
   path("index.html",views.index,name = 'index'),
   path("group_login.html",views.group_login,name = 'group_login'),
   path("",views.guide_login,name = 'guide_login'),
   path("group_register.html",views.group_register,name = 'group_register'),
   path("guide_register.html",views.guide_register,name = 'guide_register'),
   path("group_account.html",views.group_account,name = 'group_account'),
   path("guide_account.html",views.guide_account,name = 'guide_account'),
   path("all_projects.html",views.all_projects,name = 'all_projects'),
   path("submitted_projects.html",views.submitted_projects,name = 'submitted_projects'),
   path("registered_groups.html",views.registered_groups,name = 'registered_groups'),
   path("group_dashboard.html",views.group_dashboard,name = 'group_dashboard'),
   path("group_edit.html",views.group_edit,name = 'group_edit'),
   path("guide_edit.html",views.guide_edit,name = 'guide_edit'),
   path("about_us.html",views.about_us,name = 'about_us')
]