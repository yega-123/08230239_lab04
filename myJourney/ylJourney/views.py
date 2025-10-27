from django.shortcuts import render
# Import 'render' to render HTML templates with context data

from .models import AboutMe, LearningJourney
# Import the models to fetch data from the database

# View function for the home page / Learning Journey page
def index(request):
    journeys = LearningJourney.objects.all()
    # Query all records from the LearningJourney model

    return render(request, 'index.html', {'journeys': journeys})
    # Render the 'index.html' template
    # Pass the 'journeys' queryset as context to the template
    # The template can access this data using {{ journeys }}

# View function for the About Me page
def aboutMe(request):
    about = AboutMe.objects.first()
    # Get the first record from the AboutMe model
    # Assumes only one record exists for the About Me page

    return render(request, 'aboutMe.html', {'about': about})
    # Render the 'aboutMe.html' template
    # Pass the 'about' object as context to the template
    # The template can access this data using {{ about }}
