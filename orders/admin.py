from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Order, OrderItem
import datetime
from django.http import HttpResponse
import csv
from django.urls import reverse


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['content-disposition'] = 'attachment'; filename = '{}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many ]
    # write first row with header infos
    writer.writerow(field.verbose_name for field in fields)
    # write data rows
    for obj in queryset:
        data_rows = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_rows.append(value)
        writer.writerow(data_rows)
    return response


export_to_csv.short_description = 'Export to CSV'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


def admin_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(
        reverse('orders:admin_order_detail', args=[obj.id])))


def admin_order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse("orders:admin_order_pdf", args=[obj.id])))


admin_detail.allow_tags = True
admin_order_pdf.short_description = "bill pdf"


class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', admin_detail, admin_order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]


admin.site.register(Order, OrderAdmin)