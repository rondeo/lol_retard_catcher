# Generated by Django 2.2.2 on 2019-06-13 06:34

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('encrypted_id', models.CharField(max_length=100)),
                ('region', models.CharField(choices=[('euw1', 'Europe West'), ('ru', 'Россия'), ('kr', 'Republic of Korea'), ('br1', 'Brazil'), ('oc1', 'Oceania'), ('jp1', 'Japan'), ('na1', 'North America'), ('eun1', 'Europe Nordic and East'), ('tr1', 'Turkey'), ('la1', 'Latin America North'), ('la2', 'Latin America South')], max_length=50)),
                ('icon', models.CharField(blank=True, max_length=100)),
                ('level', models.PositiveIntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
