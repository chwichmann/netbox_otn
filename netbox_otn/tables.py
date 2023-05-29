import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn, columns
from .models import OMS, OCH, Channel, ChannelGroup

class OMSTable(NetBoxTable):
    name = tables.Column(
            linkify=True
            )

    channelgroup = tables.Column(
            linkify=True
            )
    status = columns.ChoiceFieldColumn()
    och_count = columns.LinkedCountColumn(
        viewname='plugins:netbox_otn:och_list',
        url_params={'och_id': 'pk'},
        verbose_name='Optical Channels'
    )

    class Meta(NetBoxTable.Meta):
        model = OMS
        fields = ('pk', 'id', 'name', 'channelgroup', 'a_end', 'z_end', 'status', 'och_count', 'comments')
        default_columns = ('name', 'channelgroup', 'a_end', 'z_end', 'status' 'och_count')

class OCHTable(NetBoxTable):
    name = tables.Column(
            linkify=True
            )
    channel = tables.Column(
            linkify=True
            )
    status = columns.ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = OCH
        fields = ('pk', 'id', 'name', 'oms', 'payload', 'channel', 'status', 'a_end', 'z_end')
        default_columns = ('name', 'payload', 'channel', 'status', 'a_end', 'z_end')

class ChannelGroupTable(NetBoxTable):
    name = tables.Column(
            linkify=True
            )

    channel_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = ChannelGroup
        fields = ('pk', 'id', 'name', 'channel_count',  'comments')
        default_columns = ('name', 'channel_count')

class ChannelTable(NetBoxTable):
    name = tables.Column(
            linkify=True
            )

    class Meta(NetBoxTable.Meta):
        model = Channel
        fields = ('pk', 'id', 'name', 'frequency', 'wavelength')
        default_columns = ('name', 'frequency', 'wavelength')
