from django.urls import path
from . import views
app_name = "api_v1"
urlpatterns = [
    path("post/",views.apiview,name="apiview"),
]