# Generated by Django 4.2.3 on 2023-07-15 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_rename_price_equipment_price_for_drivers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='product_type',
            field=models.CharField(choices=[('קרטון חד גלי 58/36/34', '1'), ('2', 'קרטון דו גלי 55/32/30'), ('3', 'קרטון חד גלי 38/30/30'), ('4', 'קרטון חד גלי'), ('5', 'כפפות בלוקים כתומות'), ('6', 'כפפות לאטקס M'), ('7', 'כפפות לאטקס L'), ('8', 'סרט דבק 66'), ('9', ' שש יח סרט דבק 66'), ('10', 'מארז סרט דבק 72 66 יח'), ('11', 'not implied'), ('12', 'not implied'), ('13', 'not implied'), ('14', 'not implied'), ('15', 'not implied'), ('16', 'not implied'), ('17', 'not implied'), ('18', 'not implied'), ('19', 'not implied'), ('20', 'not implied'), ('21', 'not implied'), ('22', 'not implied'), ('23', 'not implied'), ('24', 'not implied'), ('25', 'not implied'), ('26', 'not implied'), ('27', 'not implied'), ('28', 'not implied'), ('29', 'not implied'), ('30', 'not implied'), ('31', 'not implied'), ('32', 'not implied'), ('33', 'not implied')], max_length=100),
        ),
    ]
