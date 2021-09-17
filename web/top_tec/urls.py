from django.urls import path
from top_tec import views
app_name="top_tec"

urlpatterns = [
    # top (popular) persons
    path('', views.home, name='home_toptec'),
    # ajax path
    path('api_get_toptec/', views.api_get_toptec),
]
