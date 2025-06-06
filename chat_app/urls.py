from django.contrib import admin
from django.urls import path, include
from django.conf import settings               # ✅ Add this
from django.conf.urls.static import static    # ✅ Add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('chat.urls')),
    path('chat/', include('chat.urls')),
]

# ✅ Add this at the end to serve uploaded media files (e.g., images in posts)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
