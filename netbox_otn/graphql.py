from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import filtersets, models

class OMSType(NetBoxObjectType):

    class Meta:
        model = models.OMS
        fields = '__all__'

class OCHType(NetBoxObjectType):

    class Meta:
        model = models.OCH
        fields = '__all__'

class ChannelGroupType(NetBoxObjectType):

    class Meta:
        model = models.ChannelGroup
        fields = '__all__'
        filterset_class = filtersets.ChannelFilterSet

class ChannelType(NetBoxObjectType):

    class Meta:
        model = models.Channel
        fields = '__all__'

class Query(ObjectType):
    oms = ObjectField(OMSType)
    oms_list = ObjectListField(OMSType)

    och = ObjectField(OCHType)
    och_list = ObjectListField(OCHType)

    channelgroup = ObjectField(ChannelGroupType)
    channelgroup_list = ObjectListField(ChannelGroupType)

    channel = ObjectField(ChannelType)
    channel_list = ObjectListField(ChannelType)

schema = Query