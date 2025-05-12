from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet


router = SimpleRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'', PostViewSet, basename='posts')

urlpatterns = router.urls