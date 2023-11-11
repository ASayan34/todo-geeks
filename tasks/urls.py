from rest_framework.routers import DefaultRouter
from tasks.views import TaskAPIView

router = DefaultRouter()
router.register('', TaskAPIView)

urlpatterns = []

urlpatterns.extend(router.urls)
