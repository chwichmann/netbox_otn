from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import OMS, OCH, Channel, ChannelGroup

class NestedChannelGroupSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_otn-api:channelgroup-detail'
    )

    class Meta:
        model = Channel
        fields = ('id', 'url', 'display', 'name')

class NestedChannelSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_otn-api:channel-detail'
    )

    class Meta:
        model = Channel
        fields = ('id', 'url', 'display', 'name')

class OMSSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_otn-api:oms-detail'
    )

    channelgroup = NestedChannelGroupSerializer

    class Meta:
        model = OMS
        fields = (
            'id', 'url', 'name', 'channelgroup', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',
            )

class OCHSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_otn-api:och-detail'
    )

    class Meta:
        model = OCH
        fields = (
            'id', 'url', 'name', 'payload', 'channel', 'oms', 'tags', 'custom_fields', 'created', 'last_updated',
            )

class ChannelGroupSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_otn-api:channelgroup-detail'
    )

    channel = NestedChannelSerializer

    channel_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = ChannelGroup
        fields = (
            'id', 'url', 'name', 'channels', 'comments', 'tags', 'custom_fields', 'created', 'last_updated', 'channel_count',
            )

class ChannelSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_otn-api:channel-detail'
    )

    class Meta:
        model = Channel
        fields = (
            'id', 'url', 'name', 'frequency', 'wavelength', 'tags', 'custom_fields', 'created', 'last_updated',
            )



