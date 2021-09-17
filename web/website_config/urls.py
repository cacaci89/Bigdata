
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('topword/', include('app_top_keyword.urls')),
    path('topperson/', include('app_top_person.urls')),
    path('', include('top_tec.urls')),
    # user keyword analysis
    path('userkeyword/', include('app_user_keyword.urls')),
    # full text search and associated paragraphs for user keywords
    path('userkeyword_assoc/', include('app_user_keyword_association.urls')),
    # sentimental score for user keywords
    path('userkeyword_sentiment/', include('app_user_sentiment.urls')),
]
