# Generated by Django 3.2.5 on 2021-10-11 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthCaretsuppliestracker', '0007_auto_20211008_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='hospital',
            field=models.ForeignKey(default=0, max_length=10, on_delete=django.db.models.deletion.CASCADE, to='healthCaretsuppliestracker.hospital'),
        ),
    ]