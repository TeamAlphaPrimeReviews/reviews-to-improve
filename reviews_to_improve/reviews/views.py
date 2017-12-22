from django.shortcuts import render

# Create your views here.


def home_view(request):
    """View for rendering inital splash page."""

    return render(request, 'reviews/startbootstrap-creative-gh-pages/index.html')


def about_view(request):
    """View for rendering about us page."""

    return render(request, 'reviews/startbootstrap-full-width-pics-gh-pages/about.html')


def demo_view(request):
    """View for rendering demo page."""

    return render(request, 'reviews/startbootstrap-scrolling-nav-gh-pages/demo.html')
