from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = i18n_patterns(
    path(_('jet/dashboard/'), include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path((_('jet/')), include('jet.urls', 'jet')),  # Django JET URLS
    path("admin/", admin.site.urls),
    path(_("orders/"), include("orders.urls", namespace="orders")),
    path(_("paypal/"), include("paypal.standard.ipn.urls")),
    path(_("payment/"), include("payment.urls", namespace="payment")),
    path(_("cart/"), include("cart.urls", namespace="cart")),
    path(_("coupons/"), include("coupons.urls", namespace="coupons")),
    path("rosetta/", include("rosetta.urls")),
    path("", include("shop.urls", namespace="shop")),

)


if settings.DEBUG:
    # import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
                   # + [path('__debug__/', include(debug_toolbar.urls))]
