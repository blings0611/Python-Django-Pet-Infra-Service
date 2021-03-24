from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = 'index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('place/', include('place.urls')),
    path('themes/', include('themes.urls')),
    path('board/', include('board.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)