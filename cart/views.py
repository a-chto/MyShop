import json

from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.views.generic.list import ListView

from cart.models import Cart, CartItem
from main.models import Product


class CartItemCreateView(CreateView):
    def post(self, request, *args, **kwargs):
        """
        добавление товара в корзину
        """
        data = json.load(request.body)
        if request.user.is_authenticated():
            cart, _ = Cart.objects.get_or_create(user=request.user)
        else:
            try:
                session = Session.objects.get(session_key=request.session.session_key)
                cart, _ = Cart.objects.get_or_create(session=session)
            except Session.DoesNotExist:
                data = {
                    'success': False
                }
                return JsonResponse(data=data, status=500)
        try:
            product = Product.objects.get(id=data.get('id'))
        except Product.DoesNotExist:
            data = {
                'success': False
            }
            return JsonResponse(data=data, status=500)