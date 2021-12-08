from django.contrib import admin

from myapp.models import Currency


@admin.register(Currency)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ["id", "currency", "type", "value", "country", "book", "page", "row", "column"]
    ordering = ["id"]
    read_only_fields = ["created_ts", "updated_ts"]
    search_fields = ["currency", "country", "value"]
