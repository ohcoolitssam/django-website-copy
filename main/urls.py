"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#admin, path, include, settings and static are imported
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

#from the landing app and contact app, their views are imported
from landing.views import landing_view, project_detail_view, info_view
from contact.views import contact_view, success_view

#url patterns for all views + homepage + admin
urlpatterns = [
	path('', landing_view, name="home"),
    path('project<int:pk>/', project_detail_view, name='project_detail'),
	path('info/', info_view, name="info"),
	path('contact/', contact_view, name="other"),
	path('contact/success/', success_view, name="success"),
    path('admin/', admin.site.urls),
] 

#if debug is on, urlpatterns is altered for static and media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

