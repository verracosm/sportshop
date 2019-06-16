from django.conf.urls import url
from django.urls import path, re_path
from .views import home, baskecior, add_to_basket, delete_basket, orders, add_order

urlpatterns = [
	path('', home, name='index'),
	path('koszyk/', baskecior, name='koszyk'),
	path('zamowienie/', orders, name='orders'),
	path('zamowienie/dodaj/', add_order, name='add-order'),

	re_path(r'^koszyk/add/(?P<pk>-?\d+)/$', add_to_basket, name="add-to-basket"),
	path('koszyk/delete', delete_basket, name="delete-basket")
]