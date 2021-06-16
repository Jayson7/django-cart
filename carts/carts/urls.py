
from django.contrib import admin
from django.urls import path, include 
from apps import views
from apps.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage.as_view(), name="home"),
    path("product/<slug:slug>/", ProductView.as_view(), name="productview"),
    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"), 
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),

    path("checkout/", CheckoutView.as_view(), name="checkout"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
