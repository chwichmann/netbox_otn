from netbox.views import generic
from . import forms, models, tables
from django.db.models import Count

# OMS
class OMSView(generic.ObjectView):
    queryset = models.OMS.objects.all()

class OMSListView(generic.ObjectListView):
    queryset = models.OMS.objects.all()
    table = tables.OMSTable

class OMSEditView(generic.ObjectEditView):
    queryset = models.OMS.objects.all()
    form = forms.OMSForm

class OMSDeleteView(generic.ObjectDeleteView):
    queryset = models.OMS.objects.all()

# OCH
class OCHView(generic.ObjectView):
    queryset = models.OCH.objects.all()

class OCHListView(generic.ObjectListView):
    queryset = models.OCH.objects.all()
    table = tables.OCHTable

class OCHEditView(generic.ObjectEditView):
    queryset = models.OCH.objects.all()
    form = forms.OCHForm

class OCHDeleteView(generic.ObjectDeleteView):
    queryset = models.OCH.objects.all()

# Channel Group
class ChannelGroupView(generic.ObjectView):
    queryset = models.ChannelGroup.objects.all()

class ChannelGroupListView(generic.ObjectListView):
    queryset = models.ChannelGroup.objects.annotate(
        channel_count=Count('channels')
            )
    table = tables.ChannelGroupTable

class ChannelGroupEditView(generic.ObjectEditView):
    queryset = models.ChannelGroup.objects.all()
    form = forms.ChannelGroupForm

class ChannelGroupDeleteView(generic.ObjectDeleteView):
    queryset = models.ChannelGroup.objects.all()

# Channel
class ChannelView(generic.ObjectView):
    queryset = models.Channel.objects.all()

class ChannelListView(generic.ObjectListView):
    queryset = models.Channel.objects.all()
    table = tables.ChannelTable

class ChannelEditView(generic.ObjectEditView):
    queryset = models.Channel.objects.all()
    form = forms.ChannelForm

class ChannelDeleteView(generic.ObjectDeleteView):
    queryset = models.Channel.objects.all()
