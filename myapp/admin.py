from django.contrib import admin

from myapp import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "description", "pages", "rows_per_page", "columns_per_row"]
    ordering = ["id"]
    read_only_fields = ["created_ts", "updated_ts"]
    search_fields = ["description"]


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["id", "currency", "type", "value", "country", "book", "page", "row", "column"]
    ordering = ["id"]
    read_only_fields = ["created_ts", "updated_ts"]
    search_fields = ["currency", "country", "value"]
