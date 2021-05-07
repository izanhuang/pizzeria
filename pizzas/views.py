from django.shortcuts import render

# Create your views here.
def index(request):
    """The homepage for Pizzeria."""
    return render(request, 'pizzas/index.html')
