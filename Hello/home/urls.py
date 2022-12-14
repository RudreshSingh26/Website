# from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.views.static import serve
# from django.conf.urls import url
urlpatterns = [
    path("", views.index,name='home'),
    path("about", views.about,name='about'),
    path("product", views.product,name='product'),
    path("contact", views.contact,name='contact'),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
