from django.db import models

class Portfolino(models.Model):
	name = models.CharField(max_length = 50)
	about = models.TextField(null = True, blank = True)
	time = models.DateTimeField(auto_now_add = True, db_index = True)
	