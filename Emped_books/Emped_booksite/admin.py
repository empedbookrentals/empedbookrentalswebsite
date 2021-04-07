from django.contrib import admin
from .models import *
from django.utils.html import format_html


# Register your models here.

admin.site.site_header = 'Emped Books Private Ltd '


# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Edit', 'Name', 'IsDeleted')
    list_display_links = None

    def Edit(self, obj):
        return format_html(f'<a href="/admin/Emped_booksite/category/{obj.id}/change/" class="button default">edit</a>')


admin.site.register(Category, CategoryAdmin)


# Product Admin
class BookAdmin(admin.ModelAdmin):
    fields = ('Name', ('Image', 'preview'), 'Description', 'Genre', 'Author',
              ('Price1', 'Price2', 'Price3', 'Price4'), 'Publisher', 'Status')
    list_display = ('Edit', 'Name', 'Image', 'Description', 'Author', 'Genres',
                    'Price1', 'Price2', 'Price3', 'Price4', 'Publisher', 'Status')
    list_display_links = None
    readonly_fields = ('preview',)

    def Genres(self, obj):
        return ", ".join([b.Name for b in obj.Genre.all()])

    def Edit(self, obj):
        return format_html(f'<a href="/admin/Emped_booksite/book/{obj.id}/change/" class="button default">edit</a>')


admin.site.register(Book, BookAdmin)


# Customer Admin
class CustomerAdmin(admin.ModelAdmin):
    fields = ('PhoneNo', ('FirstName', 'LastName'), 'DoorNo', 'Address', 'LandMark', 'IsDeleted')
    list_display = ('Edit', 'PhoneNo', 'FirstName', 'LastName', 'DoorNo', 'Address', 'LandMark')
    list_display_links = None

    def Edit(self, obj):
        return format_html(f'<a href="/admin/Emped_booksite/Customer/{obj.id}/change/" class="button default">edit</a>')


admin.site.register(Customer, CustomerAdmin)


# Rent Admin
class RentAdmin(admin.ModelAdmin):
    list_display = ('Edit', 'Book', 'Customer', 'StartDate', 'Days')
    list_display_links = None

    def Edit(self, obj):
        return format_html(f'<a href="/admin/Emped_booksite/rent/{obj.id}/change/" class="button default">edit</a>')


admin.site.register(Rent, RentAdmin)
