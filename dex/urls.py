from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from p2p.views import BuyViewSet, SellViewSet, TradeViewSet
from prosumer.views import ProsumerViewSet
from users.views import UserViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Vaidyuti DEX API",
        default_version="v1",
        description="Vaidyuti DEX API for P2P trading",
        #   terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@email.com"),
        license=openapi.License(name="License Unknown"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r"prosumer/prosumers", ProsumerViewSet)
router.register(r"p2p/buy", BuyViewSet)
router.register(r"p2p/sell", SellViewSet)
router.register(r"p2p/trades", TradeViewSet)
router.register(r"users/users", UserViewSet)

urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("api/docs/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/auth/register/", include("dj_rest_auth.registration.urls")),
    path("api/v1/", include("openapi.urls")),
    path("api/v1/", include(router.urls)),
    # Swagger, Redoc and OpenAPI
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
