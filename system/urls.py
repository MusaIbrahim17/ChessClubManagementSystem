"""system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse

from clubs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('membership_application/', views.membership_application, name='membership_application'),
    path('new_club/', views.club_creation, name='new_club'),
    path('available_clubs/', views.available_clubs, name='available_clubs'),
    path('club/<int:club_id>', views.club_dashboard, name='club_dashboard'),
    path('new_tournament/<int:club_id>', views.tournament_creation, name='new_tournament'),
    path('club_memberships/', views.club_memberships, name='club_memberships'),
    path('my_applications/', views.my_applications, name='my_applications'),
    path('club/<int:club_id>/<int:user_id>/promote', views.promote_member, name='promote_member'),
    path('club/<int:club_id>/<int:user_id>/demote', views.demote_member, name='demote_member'),
    path('club/<int:club_id>/leave', views.leave_club, name='leave_club'),
    path('club/<int:club_id>/transfer_ownership/<int:user_id>', views.transfer_ownership, name='transfer_ownership'),
]
