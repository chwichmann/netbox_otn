from tabnanny import verbose
from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet
from django.urls import reverse

class Channel(NetBoxModel):
    name = models.CharField(
            verbose_name = "Channel Name",
            max_length=50
            )

    frequency = models.DecimalField(
            verbose_name = "Frequency (THz)",
            max_digits=5,
            decimal_places=2
            )

    wavelength = models.DecimalField(
            verbose_name = "Wavelength (nm)",
            max_digits=6,
            decimal_places=2
            )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_otn:channel', args=[self.pk])

class ChannelGroup(NetBoxModel):
    name = models.CharField(
            max_length=50
            )

    channels = models.ManyToManyField(
            Channel,
            related_name='channelgroup_channel'
            )

    comments = models.TextField(
            blank=True
            )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_otn:channelgroup', args=[self.pk])

class OMS(NetBoxModel):
    name = models.CharField(
        max_length=50
        )

    channelgroup = models.ForeignKey(
            to=ChannelGroup,
            on_delete=models.PROTECT,
            related_name='oms_channelgroup',
            verbose_name = "Channel Group"
            )

    comments = models.TextField(
        blank=True
        )
    class Meta:
        ordering = ('name',)
        verbose_name = 'Optical Multiplexer Section'
        verbose_name_plural = 'Optical Multiplexer Sections'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_otn:oms', args=[self.pk])


class OCHPayloadChoices(ChoiceSet):
    key = 'OCH.payload'

    CHOICES = [
            ('oduc2', 'ODUC2', 'orange'),
            ('odu4', 'ODU4', 'yellow'),
            ('odu2e', 'ODU2e','blue'),
            ('odu2', 'ODU2', 'lightblue'),
    ]

class OCH(NetBoxModel):
    oms = models.ManyToManyField(
            OMS,
            related_name='och_oms',
            blank=True,
            null=True
            )

    name = models.CharField(
            max_length=50
            )
    
    payload = models.CharField(
            max_length=50,
            choices=OCHPayloadChoices
            )

    channel = models.ForeignKey(
            to=Channel,
            on_delete=models.PROTECT,
            related_name='och_channel',
            blank=True,
            null=True
            )

    class Meta:
        ordering = ('name',)
        verbose_name = "Optical Channel"
        verbose_name_plural = "Optical Channels"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_otn:och', args=[self.pk])

    def get_payload_color(self):
        return OCHPayloadChoices.colors.get(self.payload)
