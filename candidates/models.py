from django.db import models
from django.urls import reverse
from blog.models import Post
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField

GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER_CHOICES = (
	(GENDER_MALE, 'Male'),
	(GENDER_FEMALE, 'Female'),
)

STATUS_PENDING = 'pending'
STATUS_ACCEPTED = 'accepted'
STATUS_REJECTED = 'rejected'
STATUS_CHOICES = (
	(STATUS_PENDING, 'Pending'),
	(STATUS_ACCEPTED, 'Accepted'),
	(STATUS_REJECTED, 'Rejected'),
)


class Candidate(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=GENDER_MALE)
	mobile = models.CharField(max_length=20)
	email = models.EmailField(max_length = 254)
	
	#state = USStateField(choices = STATE_CHOICES, default = ('AL', 'Alabama'))
	city = models.CharField(max_length=30)
	expected_salary = models.IntegerField()
	will_relocate = models.BooleanField(default=False)

	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)

	apply_to = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return "{} - {}".format(self.name, self.apply_to)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs = {'pk': self.apply_to.pk})