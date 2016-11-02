from searchlist_views.views import SearchListView
from searchlist_views.filters import BaseFilter
from .models import Datasets
from .forms import SearchPortalForm
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import redirect
from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PortalFilter(BaseFilter):
	search_fields = {
		"search_county" : ["county"],
		"search_theme" : ["theme"],
		"search_feature" : ["feature"],
	}


class PortalView(SearchListView):
	model = Datasets
	template_name = "portal/browse.html"
	form_class = SearchPortalForm
	filter_class = PortalFilter
	


	

def introduction(request):
	intro = loader.get_template("portal/index.html")
	return HttpResponse(intro.render())


