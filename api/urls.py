from rest_framework import routers
from . import views as api_views

router = routers.SimpleRouter()
router.register(r'users', api_views.UserViewData, basename="user-list")

urlpatterns = router.urls