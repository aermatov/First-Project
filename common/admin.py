from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin
from common.models import Footer, Banner


@admin.register(Banner)
class Banner(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Footer)
class FooterAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
