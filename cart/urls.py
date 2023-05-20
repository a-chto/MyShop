from django.urls import patch
from . import views

app_name = 'cart'
urlpatterns = path('add_to_cart/',views.CartItemCreateView.as_view(), name='add_to_cart')