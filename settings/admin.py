from django.contrib import admin
from django.utils.html import format_html
from .models import BootcampSettings


class BootcampSettingsAdmin(admin.ModelAdmin):
    list_display = ['bootcamp_title', 'opening_date', 'closing_date', 'last_update']
    list_display_links = ['bootcamp_title', 'opening_date', 'closing_date', 'last_update']
    search_fields = ['bootcamp_title', 'opening_date', 'closing_date', 'last_update']
    readonly_fields = ['last_update', 'info']
    list_per_page = 50
    show_full_result_count = True
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True

    field = ['bootcamp_title', 'opening_date', 'closing_date', 'last_update', 'info']

    # add custom field
    def info(self, obj):
        return format_html(
            "<span style='color: #454d55; padding: 10px; font-size: 13px; font-style: italic; background: #ef9a9a; border-radius: 50px;'>Bootcamp registration auto disable after closing date</span>"
        )

    # add custom field description for info
    info.short_description = 'Notice'


# register admin settings
admin.site.register(BootcampSettings, BootcampSettingsAdmin)
