from django.db import models

class Bb(models.Model):
	title = models.CharField(max_length=50, verbose_name = 'Tovar')
	content = models.TextField(null=True, blank=True, verbose_name = 'Opis')
	price = models.FloatField(null=True, blank=True, verbose_name = 'Price')
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name = 'Opublikowano')
	rubric = models.ForeignKey('Rubric', null = True, on_delete = models.PROTECT, verbose_name = "Rubrika")

	class Meta:
		verbose_name = 'Obiawlenie'
		verbose_name_plural = "Obiawlenia"
		ordering = ['-published']

class Rubric(models.Model):
	name = models.CharField(max_length = 20, db_index = True, verbose_name = "Nazwanie")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Rubriki"
		verbose_name = "Rubrika"
		ordering = ["name"]