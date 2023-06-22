# Generated by Django 4.1.7 on 2023-06-22 01:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('premium', models.BooleanField(default=1)),
                ('foto', models.ImageField(null=True, upload_to='static/perfiles/', verbose_name='Foto Perfil')),
            ],
            options={
                'verbose_name_plural': 'Perfiles',
            },
        ),
    ]