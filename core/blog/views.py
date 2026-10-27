from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView
from  .models import Post
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
 
class redirect4(RedirectView):
    url="https://biamusic.ir/"
    def get_redirect_url(self, *args, **kwargs):
        Posts = get_object_or_404(Post, pk=kwargs["pk"])
        print(Posts)
        return super().get_redirect_url(*args, **kwargs)