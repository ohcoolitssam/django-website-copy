from django.contrib import sitemaps
from django.urls import reverse
from landing.models import Project

class StaticViewSitemap(sitemaps.Sitemap):
	priority = 0.5
	changefreq = 'daily'

	def items(self):
		return ['home','project_detail', 'info', 'contact', 'success']

	def location(self, item):
		return reverse(item)
