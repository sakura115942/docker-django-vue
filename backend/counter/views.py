from rest_framework.viewsets import ModelViewSet

from .models import Counter
from .serializers import CounterSerializer


class CounterViewSet(ModelViewSet):

    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
    authentication_classes = ()
    permission_classes = ()
