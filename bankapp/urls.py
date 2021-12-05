from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt import views as jwt_views

from bankapp.views import BankDataView, BankDataDetailView

router = SimpleRouter()
router.register('branches', BankDataView)
urlpatterns=[
    path('', include(router.urls)),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('branch/<str:pk>/', BankDataDetailView.as_view(), name='branch-data'),
] + router.urls