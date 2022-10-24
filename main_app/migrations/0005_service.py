# Generated by Django 4.1.2 on 2022-10-24 21:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_boat_hours'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Service Date')),
                ('hours', models.IntegerField(verbose_name='Hours When Serviced')),
                ('services', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Engine Oil'), ('2', 'Drive Oil'), ('3', 'Fuel Filters'), ('4', 'Air Filters'), ('5', 'Impellers'), ('6', 'Engine Anodes'), ('7', 'Drive Anodes'), ('8', 'Hull Anodes'), ('9', 'Air Coolers'), ('10', 'Heat Exchangers'), ('11', 'Oil Samples'), ('12', 'Coolant Test'), ('13', 'Coolant Swap')], max_length=29, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.boat')),
            ],
        ),
    ]
