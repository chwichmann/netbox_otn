from django.db import models
from netbox.models import NetBoxModel
from . import choices
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
        return f'{self.name} ({self.frequency} THz)'

    def get_absolute_url(self):
        return reverse('plugins:netbox_otn:channel', args=[self.pk])


class ChannelGroup(NetBoxModel):
    name = models.CharField(
            max_length=50,
            unique=True,
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
    circuit = models.OneToOneField(
        to='circuits.Circuit',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='oms_circuit'
    )
    frontport_a = models.OneToOneField(
        to='dcim.FrontPort',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='oms_frontport_a',
        verbose_name = "Front port"
    )
    rearport_a = models.OneToOneField(
        to='dcim.RearPort',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='oms_rearport_a',
        verbose_name = "Rear port"
    )
    frontport_z = models.OneToOneField(
        to='dcim.FrontPort',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='oms_frontport_z',
        verbose_name = "Front port"
    )
    rearport_z = models.OneToOneField(
        to='dcim.RearPort',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='oms_rearport_z',
        verbose_name = "Rear port"
    )
    status = models.CharField(
        max_length=50,
        choices=choices.OMSStatusChoices,
        default=choices.OMSStatusChoices.STATUS_PLANNED,
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

    def get_status_color(self):
        return choices.OMSStatusChoices.colors.get(self.status)

    def a_end(self):
        if self.frontport_a and not self.rearport_a:
            return f'{self.frontport_a.device.name}: {self.frontport_a}'
        elif self.rearport_a and not self.frontport_a:
            return f'{self.rearport_a.device.name}: {self.rearport_a}'
        elif not self.rearport_a and not self.frontport_a:
            return 'No A-End'
        else:
            return 'Port Error'

    def z_end(self):
        if self.frontport_z and not self.rearport_z:
            return f'{self.frontport_z.device.name}: {self.frontport_z}'
        elif self.rearport_z and not self.frontport_z:
            return f'{self.rearport_z.device.name}: {self.rearport_z}'
        elif not self.rearport_z and not self.frontport_z:
            return 'No Z-End'
        else:
            return 'Port Error'

    def device_a(self):
        if self.frontport_a and not self.rearport_a:
            return self.frontport_a.device
        elif self.rearport_a and not self.frontport_a:
            return self.rearport_a.device

    def device_z(self):
        if self.frontport_z and not self.rearport_z:
            return self.frontport_z.device
        elif self.rearport_z and not self.frontport_z:
            return self.rearport_z.device


class OCH(NetBoxModel):
    name = models.CharField(
        max_length=50
    )
    payload = models.CharField(
        max_length=50,
        choices=choices.OCHPayloadChoices
    )
    channel = models.ForeignKey(
        to=Channel,
        on_delete=models.PROTECT,
        related_name='och_channel',
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=50,
        choices=choices.OCHStatusChoices,
        default=choices.OCHStatusChoices.STATUS_PLANNED,
    )
    #device_a = models.ForeignKey(
    #    to='dcim.Device',
    #    on_delete=models.CASCADE,
    #    related_name='och_device_a',
    #    verbose_name = "Device"
    #)
    interface_a = models.OneToOneField(
        to='dcim.Interface',
        on_delete=models.CASCADE,
        related_name='och_interface_a',
        verbose_name = "Interface"
    )
    muxport_a = models.OneToOneField(
        to='dcim.FrontPort',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='och_frontport_a',
        verbose_name = "MUX port"
    )
    interface_z = models.OneToOneField(
        to='dcim.Interface',
        on_delete=models.CASCADE,
        related_name='och_interface_z',
        verbose_name = "Interface"
    )
    muxport_z = models.OneToOneField(
        to='dcim.FrontPort',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='och_frontport_z',
        verbose_name = "MUX port"
    )
    oms = models.ManyToManyField(
        to=OMS,
        related_name='och_oms',
        blank=True,
        verbose_name='Optical Multiplexer Sections',
        help_text=('The used Optical Multiplexer Sections of this Channel (optional)')
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = "Optical Channel"
        verbose_name_plural = "Optical Channels"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_otn:och', args=[self.pk])

    def get_status_color(self):
        return choices.OCHStatusChoices.colors.get(self.status)

    def a_end(self):
        return f'{self.interface_a.device.name}: {self.interface_a}'

    def z_end(self):
        return f'{self.interface_z.device.name}: {self.interface_z}'

    def mux_a(self):
        return f'{self.muxport_a.device.name}: {self.muxport_a}'

    def mux_z(self):
        return f'{self.muxport_z.device.name}: {self.muxport_z}'


class Client(NetBoxModel):
    name = models.CharField(
        max_length=50
    )
    contract = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    och = models.ManyToManyField(
        to=OCH,
        related_name='client_och',
        verbose_name = "Optical Channel"
    )
    status = models.CharField(
        max_length=50,
        choices=choices.ClientStatusChoices,
        default=choices.ClientStatusChoices.STATUS_PLANNED,
    )
    profile = models.CharField(
        max_length=50,
        choices=choices.ClientProfileChoices,
    )
    interface_a = models.OneToOneField(
        to='dcim.Interface',
        on_delete=models.CASCADE,
        related_name='client_interface_a',
        verbose_name = "Interface"
    )
    interface_z = models.OneToOneField(
        to='dcim.Interface',
        on_delete=models.CASCADE,
        related_name='client_interface_z',
        verbose_name = "Interface"
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = "Client Signal"
        verbose_name_plural = "Client Signals"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_otn:client', args=[self.pk])

    def a_end(self):
        return f'{self.interface_a.device.name}: {self.interface_a}'

    def z_end(self):
        return f'{self.interface_z.device.name}: {self.interface_z}'