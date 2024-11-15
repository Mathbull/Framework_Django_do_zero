from django.db import models

# A herança do modelo AbstractUser permite que o novo modelo mantenha a estrutura padrão do Django, enquanto 
# ...adiciona novos campos personalizados. Isso simplifica a administração dos usuários.
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    data_nascimento = models.DateField(
        'Data de nascimento', 
        null=True, 
        blank=True
    )
    cpf = models.CharField(
        'CPF',
        max_length=11,
        null=True, 
        blank=True,
    )