# Generated by Django 4.1.9 on 2024-12-10 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('PUB', 'Published'), ('DRF', 'Draft'), ('ARC', 'Archived')], default='DRF', max_length=3)),
                ('sort', models.IntegerField(blank=True, null=True)),
                ('contact_no', models.CharField(max_length=16)),
                ('city', models.CharField(max_length=32)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='iam/users/avatar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]