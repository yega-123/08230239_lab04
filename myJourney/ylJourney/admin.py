from django.contrib import admin
# Import Django's admin module to register models for the admin interface

from .models import AboutMe, LearningJourney
# Import the models from the current app that need to be managed in the admin panel

# Register the AboutMe model to make it manageable by the Django admin site
admin.site.register(AboutMe)

# Register the LearningJourney model to make it manageable by the Django admin site
admin.site.register(LearningJourney)
