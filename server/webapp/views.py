from django.shortcuts import render

# Custom Modules
from modules.response import context

# Create your views here.
def index_view(request):
    return render(request, 'webapp/index.html', context)

def about_view(request):
    return render(request, 'webapp/about.html', context)

def contact_view(request):
    return render(request, 'webapp/contact.html', context)

def help_view(request):
    return render(request, 'webapp/index.html', context)

def faqs_view(request):
    return render(request, 'webapp/index.html', context)

def privacy_policy_view(request):
    return render(request, 'webapp/index.html', context)

def terms_conditions_view(request):
    return render(request, 'webapp/index.html', context)