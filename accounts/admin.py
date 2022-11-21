from django.contrib import admin

from accounts.models import user_details
from accounts.models import address


# Register your models here.
admin.site.register(user_details)

admin.site.register(address)


