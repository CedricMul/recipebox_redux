"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from recipe_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('recipe/<int:id>/', views.recipe_detail),
    path('author/<int:id>/', views.author_detail),
    path('add_author/', views.author_form_view),
    path('add_recipe/', views.recipe_form_view)
    #ADD DETAIL URLS
]
