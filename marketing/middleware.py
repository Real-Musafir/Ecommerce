from .models import MarketingMessage
from django.utils.deprecation import MiddlewareMixin
import datetime

class DisplayMarketing(MiddlewareMixin):
	def process_request(self, request):
		try:
			request.session['marketing_message'] = MarketingMessage.objects.get_featured_item().message
		except:
			request.session['marketing_message'] = False