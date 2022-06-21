from django.urls import path
from . import views
urlpatterns = [
    path('', views.analysisView.as_view(), name='index'),
    path('get_data', views.analysisView.get_data, name='get_data')
]