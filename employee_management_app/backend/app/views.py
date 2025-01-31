from rest_framework import viewsets
from rest_framework.response import Response
from .models import Rack, Slot
from .serializers import RackSerializer, SlotSerializer

class RackViewSet(viewsets.ModelViewSet):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer

    def create(self, request, *args, **kwargs):
        rack = Rack.objects.create(
            name=request.data['name'],
            rows=request.data['rows'],
            columns=request.data['columns']
        )
        for r in range(rack.rows):
            for c in range(rack.columns):
                Slot.objects.create(rack=rack, row=r, column=c)
        return Response(RackSerializer(rack).data)

class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

    def update(self, request, *args, **kwargs):
        slot = self.get_object()
        slot.name = request.data['name']
        slot.save()
        return Response(SlotSerializer(slot).data)
