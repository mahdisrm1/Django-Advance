from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from  .models import Post
from .forms import ContactForm
# Create your views here.
'''
TemplateView
'''
'''
##FBV 
def testview(request):
    return render(request,"index.html")
'''
##CBV
class indexviews(TemplateView):
     template_name="index.html"
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"]="ali"
        return context
"""RedirectView"""
#class redirect4(RedirectView):
#    url="https://biamusic.ir/"
#    def get_redirect_url(self, *args, **kwargs):
#        Posts = get_object_or_404(Post, pk=kwargs["pk"])
#       print(Posts)
#        return super().get_redirect_url(*args, **kwargs)
"""
ListView
"""
class listviews(ListView):
    #paginate_by = 2
    ordering = '-id'
    model = Post
    #def get_queryset(self):
    #   posts = Post.objects.filter(status=True)
    #    return posts

class detailpost(DetailView):
    model = Post

class formViews(FormView):
    template_name = "blog/formview.html"
    form_class = ContactForm
    success_url = "/blog/post/"