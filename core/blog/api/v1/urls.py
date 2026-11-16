from django.urls import path
from . import views
app_name = "api_v1"
urlpatterns = [
    path("post/",views.apiview,name="apiview"),
#    path("post/<int:id>/",views.apipost,name="apidate"),
#    path("posts/",views.apilist,name="api_list"),
    path("posts/",views.apilist.as_view(),name="apidate"),
    path("post/<int:id>/",views.apipost.as_view(),name="apidate"),
]
