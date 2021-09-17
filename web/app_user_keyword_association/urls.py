from django.urls import path
from app_user_keyword_association import views

# Namespace
app_name="namespace_user_keyword_assoc"


urlpatterns = [

    # For the association analysis page
    path('', views.home, name='home'),
    path('api_get_userkey_associate/', views.api_get_userkey_associate),

]
