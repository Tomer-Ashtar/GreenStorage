# Generated by Django 4.2.3 on 2023-07-15 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_alter_customer_totalbuys_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleshistory',
            name='customer_type',
            field=models.CharField(choices=[('new', 'New Customer'), ('return', 'Return Customer'), ('private', 'Private')], default=0, max_length=15),
            preserve_default=False,
        ),
    ]
