from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Datasets(models.Model):
	model_pic = models.ImageField(upload_to = 'media', blank=True, null=True)
	abstract_info = models.CharField(max_length=1000 ,blank=True, null=True)
	data_source = models.CharField(max_length=1000, blank=True, null=True)
	map_history = models.CharField(max_length=1000, blank=True, null=True)
	additional_info = models.CharField(max_length=1000, blank=True, null=True)
	feature_type = models.CharField(max_length=50, blank=True, null=True)
	title = models.CharField(max_length=200, blank=True, null=True)
	layer = models.CharField(max_length=30, blank=True, null=True)
	projection = models.CharField(max_length=50, blank=True, null=True)
	contact = models.CharField(max_length=100, blank=True, null=True)
	county_choices = (
		("Nairobi", "Nairobi"),("Mombasa", "Mombasa"),("Kwale", "Kwale"),
		("Kilifi", "Kilifi"),("Tana-river", "Tana-River"),("Lamu", "Lamu"),("Taita-Taveta", "Taita-Taveta"),
		("Garissa", "Garissa"),("Wajir", "Wajir"),("Mandera", "Mandera"),("Marsabit", "Marsabit"),
		("Isiolo", "Isiolo"),("Meru", "Meru"),("Tharaka-Nithi", "Tharaka-Nithi"),("Embu", "Embu"),
		("Kitui", "Kitui"),("Machakos", "Machakos"),("Makueni", "Makueni"),("Nyandarua", "Nyandarua"),
		("Nyeri", "Nyeri"),("Kirinyaga", "Kirinyaga"),("Muranga", "Muranga"),("Kiambu", "Kiambu"),
		("Turkana", "Turkana"),("West-Pokot", "West-Pokot"),("Samburu", "Samburu"),("Trans-Nzoia", "Trans-Nzoia"),
		("Uasin-Gishu", "Uasin-Gishu"),("Elgeyo-Marakwet", "Elgeyo-Marakwet"),("Nandi", "Nandi"),("Baringo", "Baringo"),
		("Laikipia", "Laikipia"),("Narok", "Narok"),("Kajiado", "Kajiado"),("Kericho", "Kericho"),
		("Bomet", "Bomet"),("Kakamega", "Kakamega"),("Vihiga", "Vihiga"),("Bungoma", "Bungoma"),
		("Busia", "Busia"),("Siaya", "Siaya"),("Kisumu", "Kisumu"),("Homa-Bay", "Homa-Bay"),
		("Migori", "Migori"),("Kisii", "Kisii"),("Nyamira", "Nyamira"),("Kwale", "Kwale"))
	county = models.CharField(max_length=30, choices=county_choices, blank=True, null=True)
	theme_choices = (
		("soil_ph", "soil_ph"),("carbon", "carbon"),("soil_depth", "soil_depth"),
		("AEZ", "AEZ"),("Temperature", "Temperature"))
	theme = models.CharField(max_length=30, choices=theme_choices, blank=True, null=True)
	feature = models.CharField(max_length=30)
	published_date = models.DateTimeField(blank=True, null=True)



	def __unicode__(self):
		return "%s %s" % (self.county, self.theme)




    