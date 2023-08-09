# Generated by Django 4.2 on 2023-06-06 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postLikes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postLikes', to='network.like'),
        ),
    ]
