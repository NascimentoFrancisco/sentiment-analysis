from django.urls import path
from .views import HomeView, SearchSentimentAnalysis

app_name = "analysis"

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('search-sentiment/', SearchSentimentAnalysis.as_view(), name='search_sentiment_analysis'),
]