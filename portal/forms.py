from django import forms

class SearchPortalForm(forms.Form):
	search_county = forms.ChoiceField(
		choices=([("",'County'),("Nairobi", "Nairobi"),("Mombasa", "Mombasa"),("Kwale", "Kwale"),
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
		("Migori", "Migori"),("Kisii", "Kisii"),("Nyamira", "Nyamira"),("Kwale", "Kwale")]),
		required=False,label='')
	search_theme = forms.ChoiceField(
		choices=([("",'Theme'),("soil_ph", "soil_ph"),("carbon", "carbon"),("soil_depth", "soil_depth"),
		("AEZ", "AEZ"),("Temperature", "Temperature")]),
		required=False, label='')
	search_feature = forms.CharField(required=False,label='',
		widget=forms.TextInput(attrs={'placeholder': 'Feature'}))
	


	