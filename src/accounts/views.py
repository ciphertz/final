from django.shortcuts import render, get_object_or_404

from shopping_cart.models import Order
from .models import Profile
from products.models import Product


# def check_product(user,product):
#     if product in user.profile.ebooks.all():
#         return True
#     else:
#         return False



def my_profile(request):
	#object_list = Product.objects.all()
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	#product_download = Product.objects.filter(download=True)
	# if product:
	#     downloadable = check_product(request.user,product)

	context = {
		'my_orders': my_orders,
		#'object_list':object_list
		#'downloadable':downloadable
	}

	return render(request, "profile.html", context)
