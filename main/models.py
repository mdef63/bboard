# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import Signal

from .utilities import *


class AdvUser(AbstractUser):
    is_actived = models.BooleanField(default=True,
                                     db_index=True,
                                     verbose_name='Прошел активацию?'
                                     )
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Слать оповещения о новых комментариях?'
                                        )

    class Meta(AbstractUser.Meta):
        pass


user_registrated = Signal(providing_args=['instance'])


def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)