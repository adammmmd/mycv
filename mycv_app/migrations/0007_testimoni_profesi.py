# Generated by Django 5.0.3 on 2024-03-28 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv_app', '0006_berita_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimoni',
            name='profesi',
            field=models.CharField(default='', max_length=200),
        ),
    ]