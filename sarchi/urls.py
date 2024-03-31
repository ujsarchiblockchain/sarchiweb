from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .utils.views import permission_denied, page_not_found, server_error

# Overrides the default 403 handler
handler403 = 'sarchi.utils.views.permission_denied'
# Overrides the default 404 handler
handler404 = 'sarchi.utils.views.page_not_found'
# Overrides the default 500 handler
handler500 = 'sarchi.utils.views.server_error'

urlpatterns = [
    # admin path
    path(f'{settings.ADMIN_PATH}/', admin.site.urls),
    # apps path
    path('', include('pages.urls')),
    path('account/', include('account.urls')),
    path('blog/', include('blog.urls')),
    path('bootcamp/', include('bootcamps.urls')),
    path('contact/', include('contact.urls')),
    path('newsletter/', include('newsletters.urls')),
    # path('event/', include('program.urls')),
    # ckeditor upload path
    path('ckeditor5/', include('django_ckeditor_5.urls'), name='ck_editor_5_upload_file'),
]

# add admin path to urlpatterns
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
