from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import UserProfile
from django.views.decorators.cache import cache_page

import sys


# Create your views here.

#@cache_page(60 * 20)  # 60 seconds/minute * 20 minutes
class Resume(TemplateView):
	template_name = 'resume.html'

	def get_context_data(self, **kwargs):
		context = {}
		context['profile'] = get_object_or_404(UserProfile)
		return context
