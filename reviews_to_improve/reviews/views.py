from django.shortcuts import render

# Create your views here.


def home_view(request):
    """View for rendering inital splash page."""

    return render(request, 'reviews/startbootstrap-creative-gh-pages/index.html')
