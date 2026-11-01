from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.views.generic.base import RedirectView

app_name = "blog"
urlpatterns = [
    #path("",views.testview,name="test1"),
    #path("2/", TemplateView.as_view(template_name="index.html",extra_context={"name":"saremi"})),
    path("3/",views.indexviews.as_view(),name="test 2"),
    #path("music/",RedirectView.as_view(url="https://biamusic.ir/"),name="music"),
    #path ("re_4/<int:pk>/",views.redirect4.as_view(),name="rediret4"),
    path("post/",views.listviews.as_view(),name="listviwes"),
    path("post/<int:pk>/",views.detailpost.as_view(),name="detailpost"),
    path("post/craete/",views.formViews.as_view(),name="formview")
]
