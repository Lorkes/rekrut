from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.list_users),
    path('users/<int:user_id>', views.user_cats),
    path('hunts/new', views.add_hunting)
]
