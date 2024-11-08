from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('order/', include('order.urls')),
    path('auth/', include('authentication.urls')),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

handler404 = 'store.views.custom_404_view'
handler500 = 'store.views.custom_500_view'
