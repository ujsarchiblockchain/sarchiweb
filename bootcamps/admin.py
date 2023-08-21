from django.contrib import admin
from django.utils.html import format_html
from .models import BootcampFirst
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from reversion_compare.admin import CompareVersionAdmin


class BootcampResource(resources.ModelResource):
    class Meta:
        model = BootcampFirst
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = (
            'first_name',
            'last_name',
            'email',
            'faculty',
            'department',
            'level',
            'application_status',
        )
        export_id_fields = '__all__'


class BootcampFirstAdmin(ImportExportModelAdmin, CompareVersionAdmin):
    resource_class = BootcampResource
    list_display = [
        'first_name',
        'last_name',
        'email',
        'faculty',
        'department',
        'level',
        'expectation',
        'application_status',
        'timestamp',
    ]
    list_display_links = [
        'first_name',
        'last_name',
        'faculty',
        'department',
        'level',
        'expectation',
        'application_status',
    ]
    search_fields = [
        'first_name',
        'last_name',
        'email',
        'faculty',
        'department',
        'level',
        'expectation',
        'application_status',
        'timestamp',
    ]
    readonly_fields = [
        'info',
    ]
    list_per_page = 50
    show_full_result_count = True
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True

    fieldsets = [
        [
            'General Information',
            {
                'classes': ['wide'],
                'fields': [
                    'first_name',
                    'last_name',
                    'email',
                    'info',
                ],
            },
        ],
        [
            'Department Summary',
            {
                'classes': ['collapse', 'wide'],
                'fields': [
                    'faculty',
                    'department',
                    'level',
                ],
            },
        ],
        [
            'Application Details',
            {
                'classes': ['collapse', 'wide'],
                'fields': [
                    'expectation',
                ],
            },
        ],
        [
            'Application Status',
            {
                'classes': ['collapse'],
                'fields': [
                    'application_status',
                ],
            },
        ],
        [
            'Last Updated',
            {
                'classes': ['collapse', 'wide'],
                'fields': [
                    'timestamp',
                ],
            },
        ],
    ]

    # add custom field
    def info(self, obj):
        return format_html(
            "<span style='color:#ef9a9a; ;'>All mails are handled automatically and delivered using signup email"
        )

    # add custom field description for info
    info.short_description = 'Notice'


# register admin settings
admin.site.register(BootcampFirst, BootcampFirstAdmin)
