from django.urls import path
# Import Django's path function to define URL patterns

from . import views
# Import views from the current app to link URLs to view functions

urlpatterns = [
    path('', views.index, name='index'),
    # URL pattern for the home page (root URL)
    # Calls the 'index' view function when the root URL is accessed
    # The 'name' parameter allows referencing this URL in templates and code

    path('about/', views.aboutMe, name='about'),
    # URL pattern for the About Me page
    # Calls the 'aboutMe' view function when '/about/' is accessed
    # The 'name' parameter allows referencing this URL in templates and code
]
