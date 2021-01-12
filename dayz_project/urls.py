
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from dayz_app.views import all_weapons


urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing_page/', include('dayz_app.urls')),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('landing_page/', all_weapons, name="landing_page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)