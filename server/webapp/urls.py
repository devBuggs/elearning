from django.urls import path

from webapp import views

app_name = 'webapp'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('help', views.help_view, name='help'),
    path('faqs', views.faqs_view, name='faqs'),
    path('privacy-policy', views.privacy_policy_view, name='privacy-policy'),
    path('terms-and-conditions', views.terms_conditions_view, name='terms-conditions'),
    path('blog', views.blog_view, name='blog'),

]