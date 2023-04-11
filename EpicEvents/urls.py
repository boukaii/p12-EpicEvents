from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from users.urls import router as test_user
from clients.urls import router as test_client
from contracts.urls import router as test_contract
from events.urls import router as test_events

router = routers.DefaultRouter()
router.registry.extend(test_user.registry)
router.registry.extend(test_client.registry)
router.registry.extend(test_contract.registry)
router.registry.extend(test_events.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
]
