from django.db import models
# Import Django's models module to define database models

# Model for the "About Me" page
class AboutMe(models.Model):
    full_name = models.CharField(max_length=100)
    # Stores the full name of the user; limited to 100 characters

    course = models.CharField(max_length=100)
    # Stores the course or program the user is enrolled in; max 100 characters

    college = models.CharField(max_length=150)
    # Stores the college or institution name; max 150 characters

    bio = models.TextField()
    # Stores a short biography of the user; allows longer text

    interests = models.TextField()
    # Stores the user’s interests or hobbies; allows longer text

    goals = models.TextField()
    # Stores the user’s personal or professional goals; allows longer text

    def __str__(self):
        return self.full_name
    # String representation of the object; useful in admin interface and shell

# Model for the "Learning Journey" page
class LearningJourney(models.Model):
    week = models.CharField(max_length=20)
    # Stores the week or session number; max 20 characters

    topic = models.CharField(max_length=200)
    # Stores the topic or activity covered in that week; max 200 characters

    what_i_learned = models.TextField()
    # Stores details of what was learned during that week; allows longer text

    reflection = models.TextField()
    # Stores the learner’s personal reflection or insights; allows longer text

    def __str__(self):
        return f"Week {self.week}: {self.topic}"
    # String representation showing the week and topic; helpful for admin display
