# Generated by Django 4.2.6 on 2023-10-22 05:51

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('id', models.UUIDField(db_comment='system user ID', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('employee_number', models.CharField(db_comment='employee number', max_length=8, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{8}$')])),
                ('username', models.CharField(db_comment='User name', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('email', models.EmailField(db_comment='email address', max_length=254, unique=True)),
                ('role', models.PositiveIntegerField(choices=[(0, 'Management'), (1, 'General'), (2, 'Part Time')], db_comment='System user role', default=2)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_comment='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, db_comment='Update date')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'User',
                'db_table_comment': 'system user',
                'ordering': ['employee_number'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
