from rest_framework.routers import DefaultRouter
from .views import ProyectoViewSet


router = DefaultRouter()
router.register(r'', ProyectoViewSet, basename='proyectos')
urlpatterns = router.urls