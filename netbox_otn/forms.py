from pickle import FALSE
from tabnanny import verbose
from typing import Required
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelBulkEditForm, NetBoxModelImportForm
from .models import OMS, OCH, Channel, ChannelGroup
from dcim.models import Site, Device, FrontPort, RearPort, Interface

from . import choices
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField

class OMSForm(NetBoxModelForm):
    site_a = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        initial_params={
            'id': '$site'
        },
        label='Site',
        required=False,
    )
    device_a = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        initial_params={
            'id': '$device'
        },
        query_params={
            'site_id': '$site_a'
        },
        label='Device',
        required=False,
    )
    frontport_a = DynamicModelChoiceField(
        queryset=FrontPort.objects.all(),
        query_params={
            'device_id': '$device_a'
        },
        required=False,
        label='Front Port',
    )
    rearport_a = DynamicModelChoiceField(
        queryset=RearPort.objects.all(),
        query_params={
            'device_id': '$device_a'
        },
        required=False,
        label='Rear Port',
    )
    site_z = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        initial_params={
            'id': '$site'
        },
        label='Site',
        required=False,
    )
    device_z = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        initial_params={
            'id': '$device'
        },
        query_params={
            'site_id': '$site_z'
        },
        label='Device',
        required=False,
    )
    frontport_z = DynamicModelChoiceField(
        queryset=FrontPort.objects.all(),
        query_params={
            'device_id': '$device_z'
        },
        required=False,
        label='Front Port',
    )
    rearport_z = DynamicModelChoiceField(
        queryset=RearPort.objects.all(),
        query_params={
            'device_id': '$device_z'
        },
        required=False,
        label='Rear Port',
    )
    comments = CommentField()

    fieldsets = (
        ('OMS Trail', ('name', 'channelgroup', 'status')),
        ('A-End', ('site_a', 'device_a', 'frontport_a', 'rearport_a' )),
        ('Z-End', ('size_z', 'device_z', 'frontport_z', 'rearport_z' )),
    )

    class Meta:
        model = OMS
        fields = ('name', 'channelgroup', 'frontport_a', 'rearport_a', 'frontport_z', 'rearport_z', 'status', 'comments')

class OMSBulkEditForm(NetBoxModelBulkEditForm):
    name = forms.CharField(
        max_length=50
    )

    channelgroup = DynamicModelChoiceField(
        queryset=ChannelGroup.objects.all()
    )

    model = OMS

class OCHForm(NetBoxModelForm):
    channel = DynamicModelChoiceField(
            queryset=Channel.objects.all()
    )
    site_a = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        initial_params={
            'id': '$site'
        },
        label='Site',
        required=False,
    )
    device_interface_a = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        label='Interface Device',
         query_params={
            'site_id': '$site_a'
        },
    )
    interface_a = DynamicModelChoiceField(
        queryset=Interface.objects.all(),
        query_params={
            'device_id': '$device_interface_a'
        },
        required=False,
        label='Interface',
    )
    device_mux_a = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        label='MUX Device',
         query_params={
            'site_id': '$site_a'
        },
    )
    muxport_a = DynamicModelChoiceField(
        queryset=FrontPort.objects.all(),
        query_params={
            'device_id': '$device_mux_a'
        },
        required=False,
        label='MUX Port',
    )
    site_z = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        initial_params={
            'id': '$site'
        },
        label='Site',
        required=False,
    )
    device_interface_z = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        label='Interface Device',
         query_params={
            'site_id': '$site_z'
        },
    )
    interface_z = DynamicModelChoiceField(
        queryset=Interface.objects.all(),
        query_params={
            'device_id': '$device_interface_z'
        },
        required=False,
        label='Interface',
    )
    device_mux_z = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        label='MUX Device',
         query_params={
            'site_id': '$site_z'
        },
    )
    muxport_z = DynamicModelChoiceField(
        queryset=FrontPort.objects.all(),
        query_params={
            'device_id': '$device_mux_z'
        },
        required=False,
        label='MUX Port',
    )
    #oms = DynamicModelChoiceField(
    #    queryset=OMS.objects.all(),
    #    #initial_params={
    #    #    'oms_id': '$oms'
    #    #},
    #    label='OMS',
    #    required=False,
    #)

    fieldsets = (
        ('Optical Channel', ('name', 'payload', 'channel', 'status')),
        ('A-End', ('site_a', 'device_interface_a', 'interface_a', 'device_mux_a', 'muxport_a')),
        ('Z-End', ('site_z', 'device_interface_z', 'interface_z', 'device_mux_z', 'muxport_z')),
        ('Optical Multiplexer Sections', ('oms',)),
    )

    class Meta:
        model = OCH
        fields = ('name', 'payload', 'channel', 'status', 'oms', 'interface_a', 'muxport_a', 'interface_z', 'muxport_z')

class OCHBulkEditForm(NetBoxModelBulkEditForm):
    name = forms.CharField(
        max_length=50
    )

    payload = forms.ChoiceField(
        choices= choices.OCHPayloadChoices
        )

    channel = DynamicModelMultipleChoiceField(
        queryset=Channel.objects.all()
    )

    model = OCH

class ChannelGroupForm(NetBoxModelForm):
    comments = CommentField()
    channels = DynamicModelMultipleChoiceField (
            queryset=Channel.objects.all()
    )
    class Meta:
        model = ChannelGroup
        fields = ('name', 'channels', 'comments')
  
class ChannelForm(NetBoxModelForm):

    class Meta:
        model = Channel
        fields = ('name', 'frequency', 'wavelength')

class ChannelImportForm(NetBoxModelImportForm):

    class Meta:
        model = Channel
        fields = ('name', 'frequency', 'wavelength')

class ChannelFilterForm(NetBoxModelFilterSetForm):
    model = Channel

    channel = forms.ModelMultipleChoiceField(
        queryset=Channel.objects.all(),
        required=False
        )
