# Generated by Django 5.1.1 on 2024-09-30 10:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0014_alter_customer_options_remove_customer_email_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"permissions": [("cancel_order", "Can cancel Order")]},
        ),
    ]
