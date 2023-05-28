from operator import truediv
from pickle import TRUE
import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import OMS, OCH, Channel, ChannelGroup

class OMSTable(NetBoxTable):
    name = tables.Column(
            linkify=True
            )

    channelgroup = tables.Column(
            linkify=True
            )

    class Meta(NetBoxTable.Meta):
        model = OMS
        fields = ('pk', 'id', 'name', 'channelgroup', 'status', 'comments')
        default_columns = ('name', 'channelgroup')

class OCHTable(NetBoxTable):
    name = tables.Column(
            linkify=True
            )
    payload = ChoiceFieldColumn()
    channel = tables.Column(
            linkify=True
            )

    class Meta(NetBoxTable.Meta):
        model = OCH
        fields = ('pk', 'id', 'name', 'oms', 'payload', 'channel', 'status',)
        default_columns = ('name', 'payload', 'channel', 'status')

class ChannelGroupTable(NetBoxTable):
    name = tables.Column(
            linkify=True
            )

    channel_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = ChannelGroup
        fields = ('pk', 'id', 'name', 'channels', 'channel_count',  'comments')
        default_columns = ('name', 'channel_count')

class ChannelTable(NetBoxTable):
    name = tables.Column(
            linkify=True
            )

    class Meta(NetBoxTable.Meta):
        model = Channel
        fields = ('pk', 'id', 'name', 'frequency', 'wavelength')
        default_columns = ('name', 'frequency', 'wavelength')
