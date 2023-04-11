from rest_framework import viewsets
from contracts.models import Contract
from contracts.serializers import ContractSerializer


class ContractViewSet(viewsets.ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
