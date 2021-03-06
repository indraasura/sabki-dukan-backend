from django.contrib import admin
from django.urls import path, include
from . import views
 
urlpatterns = [
	path('products/', views.ListProductView.as_view(), name="products-all"),
	path('register/', views.register_view, name="register_user"),
	path('verify/', views.verify_otp_view, name="verify_otp"),
	path('transaction/', views.transaction_view, name="transaction_user"),
	path('payment/', views.payment_view, name="payment_update"),
	path(r'image/(?<user_id>\w+)/$', views.image_view, name="image_view")
]