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
    return render(request, 'webapp/help.html', context)

def faqs_view(request):
    return render(request, 'webapp/faqs.html', context)

def privacy_policy_view(request):
    return render(request, 'webapp/privacy-policy.html', context)

def terms_conditions_view(request):
    return render(request, 'webapp/terms-conditions.html', context)

def course_view(request):
    return render(request, 'webapp/courses.html', context)

# Global Errors
def custom_page_not_found_view(request, exception):
    context['segment'] = '404'
    return render(request, "webapp/error.html", context)

def custom_error_view(request, exception=None):
    context['segment'] = '500'
    return render(request, "webapp/error.html", context)

def custom_permission_denied_view(request, exception=None):
    context['segment'] = '403'
    return render(request, "webapp/error.html", context)

def custom_bad_request_view(request, exception=None):
    context['segment'] = '400'
    return render(request, "webapp/error.html", context)

