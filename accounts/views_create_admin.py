# accounts/views_create_admin.py

from django.contrib.auth import get_user_model
from django.http import HttpResponse

def create_superuser(request):
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin123")
        return HttpResponse("✅ Superuser created: admin / admin123")
    else:
        return HttpResponse("⚠️ Superuser already exists.")
