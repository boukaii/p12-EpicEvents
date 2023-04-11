from rest_framework import routers
from contracts.views import ContractViewSet

router = routers.DefaultRouter()
router.register('contract', ContractViewSet)
