from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
path("pay/", phonepay),
path("redirect/", payment_callback),
path("redirect/callback/", callbackv),
]

