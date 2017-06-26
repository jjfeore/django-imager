"""Define views for imagersite."""


from django.shortcuts import render


def home_view(request):
    """Home view callable, for the home page."""
    context = {'page': ' | Home'}
    return render(request, 'imagersite/home.html', context=context)


def account_view(request):
    """User account profile view."""
    return render(request, 'imagersite/account.html')
