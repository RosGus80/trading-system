from django.contrib import admin

from main.models import Factory, Retailer, Entrepreneur


# Register your models here.


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'total_supplier_debt',)
    list_filter = ('city', )
    search_fields = ('city', )

    actions = ('clear_supplier_debt', )

    def clear_supplier_debt(self, request, queryset):
        queryset.update(total_supplier_debt=0)


@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'total_supplier_debt',)
    list_filter = ('city', )
    search_fields = ('city', )

    actions = ('clear_supplier_debt', )

    def clear_supplier_debt(self, request, queryset):
        queryset.update(total_supplier_debt=0)


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'total_supplier_debt',)
    list_filter = ('city', )
    search_fields = ('city', )

    actions = ('clear_supplier_debt', )

    def clear_supplier_debt(self, request, queryset):
        queryset.update(total_supplier_debt=0)
