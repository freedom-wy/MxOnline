from django.urls import path
from .views import ChatIndexView


urlpatterns = [
    path("", ChatIndexView.as_view(), name="index")
]

