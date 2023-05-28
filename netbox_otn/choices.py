from utilities.choices import ChoiceSet

class OCHPayloadChoices(ChoiceSet):
    key = 'OCH.payload'

    CHOICES = [
            ('oduc2', 'ODUC2'),
            ('odu4', 'ODU4'),
            ('odu2e', 'ODU2e'),
            ('odu2', 'ODU2'),
    ]

class OMSStatusChoices(ChoiceSet):
    key = 'OMS.status'

    STATUS_OFFLINE = 'offline'
    STATUS_ACTIVE = 'active'
    STATUS_PLANNED = 'planned'
    STATUS_DECOMMISSIONING = 'decommissioning'

    CHOICES = [
        (STATUS_OFFLINE, 'Offline', 'gray'),
        (STATUS_ACTIVE, 'Active', 'green'),
        (STATUS_PLANNED, 'Planned', 'cyan'),
        (STATUS_DECOMMISSIONING, 'Decommissioning', 'yellow'),
    ]

class OCHStatusChoices(ChoiceSet):
    key = 'OCH.status'

    STATUS_OFFLINE = 'offline'
    STATUS_ACTIVE = 'active'
    STATUS_PLANNED = 'planned'
    STATUS_DECOMMISSIONING = 'decommissioning'

    CHOICES = [
        (STATUS_OFFLINE, 'Offline', 'gray'),
        (STATUS_ACTIVE, 'Active', 'green'),
        (STATUS_PLANNED, 'Planned', 'cyan'),
        (STATUS_DECOMMISSIONING, 'Decommissioning', 'yellow'),
    ]