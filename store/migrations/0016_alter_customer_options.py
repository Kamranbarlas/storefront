# Generated by Django 4.2.16 on 2024-10-02 16:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0015_alter_order_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customer",
            options={
                "ordering": ["user__first_name", "user__last_name"],
                "permissions": [("view_history", "can_view_history")],
            },
        ),
    ]
