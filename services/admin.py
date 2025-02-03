from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import Service, Appointment, Review, GalleryImage, Contact


admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Review)
admin.site.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['image']

@admin.action(description='Экспортировать в CSV')
def export_contacts_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contacts.csv"'
    writer = csv.writer(response)
    writer.writerow(['ФИО', 'Номер телефона', 'Дата создания'])
    
    for contact in queryset:
        writer.writerow([contact.full_name, contact.phone_number, contact.created_at])
    
    return response

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'created_at')
    search_fields = ('full_name', 'phone_number')
    list_filter = ('created_at',)
    actions = [export_contacts_to_csv]