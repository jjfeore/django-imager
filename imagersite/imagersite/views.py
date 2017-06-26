"""Define views for imagersite."""


from django.shortcuts import render


def home_view(request):
    """Return the home view."""
    context = {
        'stuff': 'Put this in the page',
        'page': 'Home'
    }
    return render(request, 'imagersite/home.html', content=context)
