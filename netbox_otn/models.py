from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet
from django.urls import reverse

class OMS(NetBoxModel):
    name = models.CharField(
        max_length=50
        )
    comments = models.TextField(
        blank=True
        )
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_otn:OMS', args=[self.pk])

class Channel(NetBoxModel):
    name = models.CharField(
            max_length=50
            )

    frequency = models.DecimalField(
            max_digits=3,
            decimal_places=2
            )

    wavelength = models.DecimalField(
            max_digits=4,
            decimal_places=2
            )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.mame

    def get_absolute_url(self):
        return reverse('plugins:netbox_otn:Channel', args=[self.pk])

class OCHPayloadChoices(ChoiceSet):
    key = 'OCH.payload'

    CHOICES = [
            ('oduc2', 'ODUC2'),
            ('odu4', 'ODU4'),
            ('odu2e', 'ODU2e'),
            ('odu2', 'ODU2'),
    ]

class OCH(NetBoxModel):
    access_list = models.ForeignKey(
        to=OMS,
        on_delete=models.PROTECT,
        related_name='OMS'
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
            related_name='OCH',
            blank=True,
            null=True
            )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_otn:OCH', args=[self.pk])

class ChannelGroup(NetBoxModel):
    name = models.CharField(
            max_length=50
            )

    channels = models.ManyToManyField(
            Channel
            )

    comments = models.TextField(
            blank=True
            )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_otn:ChannelGroup', args=[self.pk])
