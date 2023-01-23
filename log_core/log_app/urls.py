from django.urls import path
from . import views
from .views import signup, Login

urlpatterns = [
    path('home', views.home, name='home'),
    path('signup', signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', views.logout, name='logout'),
    path('student', views.student, name='student'),
    path('team_lead/', views.team_lead, name='team_lead'),
    # path('role/specific_student/', views.Role, name='role'),
    path('role/specific_student/', views.Role, name='role'),
    path('SpecificRole', views.SpecificRole, name='SpecificRole')
]
