
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, post, category, index
# from django.conf.urls import url

urlpatterns = [
    path('home/',home),
    path('index/',index),
    path('curiosity/<slug:url>', post),
    path('category/<slug:url>',category)
]

# This was written by Sushant Abrin
