from pickle import FALSE
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelBulkEditForm, NetBoxModelCSVForm
from .models import OMS, OCH, Channel, ChannelGroup, OCHPayloadChoices
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField

class OMSForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = OMS
        fields = ('name', 'channelgroup', 'comments')

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
    class Meta:
        model = OCH
        fields = ('name', 'payload', 'channel')

class OCHBulkEditForm(NetBoxModelBulkEditForm):
    name = forms.CharField(
        max_length=50
    )

    payload = forms.ChoiceField(
        choices= OCHPayloadChoices
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

class ChannelCSVForm(NetBoxModelCSVForm):

    class Meta:
        model = Channel
        fields = ('name', 'frequency', 'wavelength')

class ChannelFilterForm(NetBoxModelFilterSetForm):
    model = Channel

    channel = forms.ModelMultipleChoiceField(
        queryset=Channel.objects.all(),
        required=False
        )
