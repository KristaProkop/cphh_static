
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.cphh.models import Message, Inquiry



class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)

class InquiryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Inquiry, InquiryAdmin)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.cphh.urls', namespace='cphh')),
]
