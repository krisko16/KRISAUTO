# Generated by Django 4.2.3 on 2023-07-28 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('power_hp', models.IntegerField(max_length=4)),
                ('year', models.IntegerField(max_length=4)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='vehicle_images')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='vehicle.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
