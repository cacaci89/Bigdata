from django.urls import path
from app_user_keyword import views

app_name="app_user_keyword"

urlpatterns = [
    # For the user userkey analysis page
    path('', views.home, name='home'),
    path('api_get_top_userkey/', views.api_get_top_userkey),
]
