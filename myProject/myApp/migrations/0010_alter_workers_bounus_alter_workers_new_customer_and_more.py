# Generated by Django 4.2.3 on 2023-07-15 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_saleshistory_sales_man'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='bounus',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='workers',
            name='new_customer',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='workers',
            name='return_customers',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='workers',
            name='sum_of_sales',
            field=models.JSONField(default=dict, null=True),
        ),
    ]
