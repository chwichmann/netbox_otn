from netbox.forms import NetBoxModelForm
from .models import OMS, OCH, Channel, ChannelGroup
from utilities.forms.fields import CommentField, DynamicModelChoiceField

class OMSForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = OMS
        fields = ('name', 'comments')

class OCHForm(NetBoxModelForm):
    channel = DynamicModelChoiceField(
            queryset=Channel.objects.all()
    )
    class Meta:
        model = OCH
        fields = ('name', 'payload', 'channel')

class ChannelGroupForm(NetBoxModelForm):
    comments = CommentField()
    channels = DynamicModelChoiceField(
            queryset=Channel.objects.all()
    )
    class Meta:
        model = ChannelGroup
        fields = ('name', 'channels', 'comments')

class ChannelForm(NetBoxModelForm):

    class Meta:
        model = Channel
        fields = ('name', 'frequency', 'wavelength')
