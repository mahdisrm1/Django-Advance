from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("",views.testview,name="test1"),
    #path("2/", TemplateView.as_view(template_name="index.html",extra_context={"name":"saremi"})),
    path("3/",views.indexviews.as_view(),name="test 2")
]