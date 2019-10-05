from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.parsers import JSONParser
from .models import Product, PhoneUser, Transactions, ReceiptModel
from .serializers import ProductsSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import PhoneUserSerializer

import razorpay
client = razorpay.Client(auth=("rzp_test_GdHGJX8WrUESu5", "HMXulhyeBwsaFZUk9u1rqyMe"))

class ListProductView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductsSerializer

def image_view(request, user_id):
	print(user_id)

from .models import PhoneUser
@csrf_exempt
def register_view(request):

	context = {}
	if request.method=='POST':
		#print("json men", request.POST.get("phone"), request.POST, JSONParser().parse(request) )
		my_json = JSONParser().parse(request)
		my_phone = my_json.get("phone_number")#.get("title")
		print(my_phone, "FLOAAAAA")
		rg = PhoneUser(phone_number=my_phone)
		rg.save()
		my_obj = PhoneUser.objects.order_by("-phone_id")[0]
		print(my_obj, my_obj.phone_number, my_obj.otp)
		serializer = PhoneUserSerializer(data=my_json)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

	#add sms feature
	#call view to create transaction

@csrf_exempt
def verify_otp_view(request, *args, **kwargs):

	if request.method == "POST":
		my_json = JSONParser().parse(request)
		my_otp = my_json.get("otp")
		my_obj = PhoneUser.objects.order_by("-phone_id")[0]
		print(my_obj.otp, my_otp)
		if my_obj.otp == my_otp:
			return JsonResponse({"response": "otp matched"})
		else:
			return JsonResponse({"error":"enter OTP again"})#reload page


@csrf_exempt
def transaction_view(request, *args, **kwargs):

	context = []
	totalSum = 0 
	if request.method == 'POST':
		''' JSON structure -> {"phone": 9685847170, p_list : [ {p_id: uuid, title:.., other....}, 
																{p_id: uuid, title:.., other....},
																{p_id: uuid, title:.., other....} ] }'''
		my_json = JSONParser().parse(request)
		p_list = my_json.get("p_list")
		my_phone = my_json.get("phone")
		#print(p_list)
		phone = PhoneUser.objects.filter(phone_number=my_phone)[0]
		#print(phone)
		for trans in p_list:
			#print(trans["title"])
			prod = Product.objects.filter(title = trans.get("title"))[0]
			#print("prod", prod)
			#print("id", phone.phone_id)
			#print("p_id", prod.p_id)
			#print("trans", trans)
			price = Product.objects.get(p_id=prod.p_id).price
			totalSum += price
			# Transactions.objects.create(fk_phone=phone.id, fk_p_id=prod.get("p_id"), quantity=trans["quantity"])
			tr = Transactions(fk_phone_id=phone.phone_id, fk_p_id_id=prod.p_id, quantity=trans["quantity"])
			tr.save()

			context.append({"fk_phone":phone.phone_id, "fk_p_id":prod.p_id, "quantity":trans["quantity"]})

		rc = ReceiptModel(price=totalSum)
		receipt_id = rc.receipt_id
		#print("order ke liye:", int(totalSum*100), receipt_id)
		order = client.order.create({"amount":int(totalSum*100), "currency":"INR", "receipt":str(receipt_id), "payment_capture": 1})
		rc.order_id = order["id"]
		#print("this is ", order)
		#print(receipt_id)
		rc.save()
		context.append({"totalSum": totalSum, "receipt_id":receipt_id, "order_id":rc.order_id})
		print(context)
	
	return JsonResponse(context, safe=False)#return view with success transaction created

@csrf_exempt
def payment_view(request):
	my_json = JSONParser().parse(request)
	rc = ReceiptModel.objects.get(order_id=my_json.get("order_id", False))
	rc.payment_id = my_json.get("payment_id", False)
	rc.save()
	return JsonResponse({"idddd": rc.payment_id})