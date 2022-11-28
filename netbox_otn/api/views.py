from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from .. import filtersets, models
from .serializers import OMSSerializer, OCHSerializer, ChannelGroupSerializer, ChannelSerializer

class OMSViewSet(NetBoxModelViewSet):
    queryset = models.OMS.objects.prefetch_related('tags')
    serializer_class = OMSSerializer

class OCHViewSet(NetBoxModelViewSet):
    queryset = models.OCH.objects.prefetch_related('tags')
    serializer_class = OCHSerializer

class ChannelGroupViewSet(NetBoxModelViewSet):
    queryset = models.ChannelGroup.objects.prefetch_related('tags').annotate(
        channel_count=Count('channels')
        )
    serializer_class = ChannelGroupSerializer

class ChannelViewSet(NetBoxModelViewSet):
    queryset = models.Channel.objects.prefetch_related('tags')
    serializer_class = ChannelSerializer