# Generated by Django 4.2.3 on 2023-07-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_equipment_origin_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='package',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
