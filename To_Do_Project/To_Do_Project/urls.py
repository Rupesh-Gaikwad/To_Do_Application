"""to_do_Project URL Configuration

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
from django.urls import path, include
from to_do_App import views
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view),
    path('signup/', views.sign_up_view),
    path('accounts/', include(urls)),
    path('ongoing_tasks/', views.ongoing_tasks_view),
    path('upcoming_tasks/', views.upcoming_tasks_view),
    path('completed_tasks/', views.completed_tasks_view),
    path('tasks_history/', views.tasks_history_view),
    path('new_task/', views.new_tasks_view),
]
