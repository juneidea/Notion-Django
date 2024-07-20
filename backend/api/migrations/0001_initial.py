# Generated by Django 4.2.14 on 2024-07-18 19:33

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
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_archived', models.BooleanField()),
                ('parent_id', models.IntegerField(blank=True, default=-1)),
                ('content', models.TextField(blank=True)),
                ('cover_image', models.CharField(blank=True, max_length=500)),
                ('icon', models.CharField(blank=True, max_length=500)),
                ('is_published', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
