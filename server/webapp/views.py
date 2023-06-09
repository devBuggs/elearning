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

def blog_view(request):
    return render(request, 'webapp/blog-index.html', context)














# Global Errors
def custom_bad_request_view(request, exception=None):
    error = {
        "segment": "400"
    }
    context.update(error)
    return render(request, "webapp/error.html", context)

def custom_permission_denied_view(request, exception=None):
    error = {
        "segment": "403"
    }
    context.update(error)
    return render(request, "webapp/error.html", context)

def custom_page_not_found_view(request, exception):
    error = {
        "segment": "404"
    }
    context.update(error)
    return render(request, "webapp/error.html", context)

def custom_error_view(request, exception=None):
    error = {
        "segment": "500"
    }
    context.update(error)
    return render(request, "webapp/error.html", context)
