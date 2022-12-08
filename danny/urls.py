from django.urls import path
from danny import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('checkout/',views.checkout,name="checkout"),
    path('cart/',views.cart,name="cart"),
    path('lienhe/',views.lienhe,name="lienhe"),
    path('store/login/',views.login,name="login"),
    path('list/',views.member_list,name="rq_register"),
    path('register/cart/',views.cart,name="cart"),
    path('register/checkout/',views.checkout,name="checkout"),
    path('register/cart/checkout/',views.checkout,name="checkout"),
    path('',views.index),
    path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]