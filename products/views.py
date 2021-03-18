from django.shortcuts import render,Http404
from .models import Product, ProductImage
# Create your views here.
from marketing.models import MarketingMessage

def search(request):
	try:
		q = request.GET.get('q')
	except:
		q=none
	if q:
		products = Product.objects.filter(title__icontains=q)
		context = {'query':q, 'products': products }
		template = 'products/results.html'
	else:
		template='products/home.html'
		context={}
	return render(request, template, context)

def home(request):
	products = Product.objects.all()
	marketing_message = MarketingMessage.objects.all()[0]
	template = 'products/home.html'
	context = {"products": products}
	return render(request, template, context)


def all(request):
	products=Product.objects.all()
	context = {'products':products}
	template='products/all.html'
	return render(request, template, context)

def single(request, slug):
	try:
		product = Product.objects.get(slug=slug)
		#images = product.productimage_set.all()
		images = ProductImage.objects.filter(product=product)
		context = {'product':product, "images": images}
		template='products/single.html'
		return render(request, template, context)
	except:
		raise Http404
