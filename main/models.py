# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


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
