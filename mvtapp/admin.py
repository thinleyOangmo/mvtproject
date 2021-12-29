from django.contrib import admin
from mvtapp.models import Webdevelopment_Details
# Register your models here.
class Webdevelopment_DetailsAdmin(admin.ModelAdmin):
	'''Admin view for Webdevelopment_Details'''
	list_display=('did','name','age','phone_no','gender')

admin.site.register(Webdevelopment_Details,Webdevelopment_DetailsAdmin)
