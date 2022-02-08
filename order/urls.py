from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet)
router.register(r'reviews', OrderReviewViewSet)
urlpatterns = router.urls