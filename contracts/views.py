from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from contracts.models import Contract
from contracts.serializers import ContractSerializer
from contracts.permissions import IsSaleEmployeeConnectedToTheContractOrReadOnly, IsSupportEmployeeOrReadOnly


class ContractViewSet(viewsets.ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated,
                          IsSaleEmployeeConnectedToTheContractOrReadOnly,
                          IsSupportEmployeeOrReadOnly]
