from django.db import models

from carts.models import Cart
from django.contrib.auth import get_user_model
User = get_user_model()

STATUS_CHOICES=(

	("Started", "Started"),
	("Abandoned", "Abandoned"),
	("Finished", "Finished"),
)

class Order(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	order_id = models.CharField(max_length=120, unique=True)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
	
	sub_total = models.DecimalField(default=10.99,max_digits=1000,decimal_places=2)
	tax_total = models.DecimalField(default=0.00,max_digits=1000,decimal_places=2)
	final_total = models.DecimalField(default=10.99,max_digits=1000,decimal_places=2)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return self.order_id