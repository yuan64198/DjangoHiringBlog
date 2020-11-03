from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.

# position_name = models.CharField(max_length=100)
# text_decription = models.TextField(null=True, blank=True)
# min_age = models.IntegerField(default=18)
# max_age = models.IntegerField(default=65)
# salary = models.IntegerField()
# #state = USStateField(choices = STATE_CHOICES)
# city = models.CharField(max_length=30)
# n_openings = models.IntegerField(default=0)

# author = models.ForeignKey(User, on_delete=models.CASCADE)
# date_posted = models.DateTimeField(default=timezone.now)


class BlogTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username = 'test', email = 'test@gmail.com', password = 'Test123456')
        Post.objects.create(position_name = 'SE', text_decription='foo bar', min_age = 18, max_age = 65, salary = 100000, city='Austin', n_openings = 100, author = user)

    
    def test_post_info(self):
        post = Post.objects.get(position_name = 'SE')
        self.assertEqual(str(post), 'SE') 