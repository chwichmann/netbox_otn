import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import OMS, OCH, Channel, ChannelGroup

class OMSTable(NetBoxTable):
    name = tables.Column(
            linkify=True
            )

    class Meta(NetBoxTable.Meta):
        model = OMS
        fields = ('pk', 'id', 'name', 'comments')
        default_columns = ('name')

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
        fields = ('pk', 'id', 'name', 'payload', 'channel')
        default_columuns = ('name', 'payload', 'channel')

class ChannelGroupTable(NetBoxTable):
    name = tables.Column(
            linkify=True
            )

    channel_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = ChannelGroup
        fields = ('pk', 'id', 'name', 'channels', 'channel_count',  'comments')
        default_columns = ('name', 'channel_count')

class Channel(NetBoxTable):
    name = tables.Column(
            linkify=True
            )

    class Meta(NetBoxTable.Meta):
        model = Channel
        fields = ('pk', 'id', 'name', 'frequency', 'wavelength')
        default_columns = ('name', 'frequency', 'wavelength')
