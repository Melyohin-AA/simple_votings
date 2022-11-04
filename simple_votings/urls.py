"""simple_votings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from main.views import views
from main.views import testing_api_view
from django.contrib.auth import views as auth_views
from main.views.views import get_menu_context

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cad/', views.clear_all_data_page),
    path('testing_api/', testing_api_view.TestingApiView.as_view()),
    path('', views.index_page),
    path('login/', auth_views.LoginView.as_view(extra_context={'menu': get_menu_context(), 'pagename': 'Авторизация'})),
    path('logout/', auth_views.LogoutView.as_view()),
    path('registration/', views.registration_page),
    path('vm/my_votings/', views.my_votings_page),
    path('vm/new_voting/', views.new_voting_page),
    path('vote/<int:id>/', views.vote_page),
    path('search_v/', views.voting_search_page),
    path('voting_info/<int:id>/', views.voting_info_page),
    path('profile/<int:id>/', views.profile_page),
    path('my_profile/', views.my_profile_page),
    path('manage_voting/<int:id>/', views.manage_voting_page),
]
