from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Experience, Education, UserProfile

import sys
# Create your views here.


class Resume(TemplateView):

	template_name = 'resume.html'

	def get_context_data(self, **kwargs):
		context = {}
		context['profile'] = get_object_or_404(UserProfile)
		return context