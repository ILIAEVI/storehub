from django.contrib import admin
from order.models import UserCart


@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)
    search_fields = ('user__email',)

