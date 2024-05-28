from rest_framework.routers import DefaultRouter
from views.company_views import (
    CompanyListViewSet,
    CompanyCreateViewSet,
    CompanyRetrieveViewSet,
    CompanyUpdateViewSet,
    CompanyDestroyViewSet
)

app_name = 'Company'
router = DefaultRouter()

router.register(r'Company-list', CompanyListViewSet, basename='Company-list')
router.register(r'Company-create', CompanyCreateViewSet, basename='Company-create')
router.register(r'Company-retrieve', CompanyRetrieveViewSet, basename='Company-retrieve')
router.register(r'Company-update', CompanyUpdateViewSet, basename='Company-update')
router.register(r'Company-destroy', CompanyDestroyViewSet, basename='Company-destroy')

urlpatterns = router.urls
