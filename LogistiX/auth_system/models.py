
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from warehouse_management.models import Warehouse


class CustomUser(AbstractUser):
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',  # Измененное имя связи для пользовательской модели.
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',  # Измененное имя связи для пользовательской модели.
        related_query_name='user',
    )


class Role(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission, blank=True)


# # Присвоение разрешений
# content_type = ContentType.objects.get_for_model(Warehouse)  # Получаем тип контента для модели склада
# permission1 = Permission.objects.create(codename='can_view_inventory', name='Can view inventory',
#                                         content_type=content_type)
# permission2 = Permission.objects.create(codename='can_manage_inventory', name='Can manage inventory',
#                                         content_type=content_type)
#
# # Присвоение разрешений роли "менеджер склада"
# manager_role = Role.objects.get(name='Warehouse Manager')
# manager_role.permissions.add(permission1, permission2)