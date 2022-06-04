from django.shortcuts import render
from django.views import View

from .models import *
# Create your views here.

class BaseView(View):
	views = {}
	views['categories'] = Category.objects.all()
	views['subcategories'] = SubCategory.objects.all()



class HomeView(BaseView):
	def get(self,request):
		self.views
		self.views['new_produts'] = Product.objects.filter(labels = 'new')
		self.views['hot_produts'] = Product.objects.filter(labels = 'hot')
		self.views['offer_produts'] = Product.objects.filter(labels = 'offer')
		self.views['sliders'] = Slider.objects.all()
		self.views['ads'] = Ad.objects.all()

		return render(request,'index.html',self.views)

class SubCategoryView(BaseView):
	def get (self,request,slug):
		subcat_id =SubCategory.objects.get(slug = slug).id
		self.views['subcat_products'] = Product.objects.filter(subcateogry_id = subcat_id)
		return render(request,'index.html',self.views)

class DetailView(BaseView):
	def get(self,request,slug):
		self.views['detail_product'] = Product.objects.filter(slug = slug)
		return render(request,'single.html',self.views)	