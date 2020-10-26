from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField
# STATE_OPTIONS = (
#     "Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", 
#     "California", "Colorado", "Connecticut", "District of Columbia", 
#     "Delaware", "Florida", "Georgia", "Guam", "Hawaii", 
#     "Iowa", "Idaho", "Illinois", "Indiana", 
#     "Kansas", "Kentucky", "Louisiana", 
#     "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", 
#     "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", 
#     "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", 
#     "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", 
#     "Utah", "Virginia", "Virgin Islands", "Vermont", 
#     "Washington", "Wisconsin", "West Virginia", "Wyoming",
# )


class Post(models.Model):
    """
    Position Name
    Text Decription
    Age Criteria
    Salary
    No. of openings
    """
    # job_title = models.CharField(max_length=100)
    # comparny_name = models.CharField(max_length=100, default="Nan")
    # location = models.CharField(max_length=100, default="Nan")
    # salary = models.CharField(max_length=100, default="0")
    # content = models.TextField()
    # 
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    position_name = models.CharField(max_length=100)
    text_decription = models.TextField(null=True, blank=True)
    min_age = models.IntegerField(default=18)
    max_age = models.IntegerField(default=65)
    salary = models.IntegerField()
    state = USStateField(choices = STATE_CHOICES, default = ('AL', 'Alabama'))
    n_openings = models.IntegerField(default=0)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.position_name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# class Application(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100, default="Nan")
    

#     def __str__(self):
#         return self.name