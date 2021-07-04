from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

class ProductsView(generic.TemplateView):
    template_name = "products.html"

class AboutView(generic.TemplateView):
    template_name = "about.html"