from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),

    # Uygulama yolları
    path('games/', include('games.urls')),
    path('cards/', include('cards.urls')),
    path('blog/', include('blog.urls')),
    path('comments/', include('comments.urls')),
    path('favorites/', include('favorites.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include(('pages.urls', 'pages'), namespace='pages')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)