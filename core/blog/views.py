from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
def testview(request):
    return render(request,"index.html")

class indexviews(TemplateView):
     template_name="index.html"
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"]="ali"
        return context