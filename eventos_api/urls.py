from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, ParticipanteViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet, basename='evento')
router.register(r'participantes', ParticipanteViewSet, basename='participante')

urlpatterns = router.urls