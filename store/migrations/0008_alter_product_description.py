# Generated by Django 4.2.7 on 2024-08-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0007_alter_collection_options_alter_customer_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
