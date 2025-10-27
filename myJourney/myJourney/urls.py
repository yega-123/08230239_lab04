"""
URL configuration for myJourney project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# Import Django's admin module to include the admin interface

from django.urls import path, include
# Import 'path' to define URL patterns
# Import 'include' to include URL patterns from other apps

urlpatterns = [
    path('admin/', admin.site.urls),
    # URL pattern for the Django admin interface
    # When 'admin/' is accessed, Django serves the admin site

    path('', include('ylJourney.urls')),
    # Include all URL patterns from the 'ylJourney' app
    # The empty string '' means the app's URLs are loaded at the root of the project
]


