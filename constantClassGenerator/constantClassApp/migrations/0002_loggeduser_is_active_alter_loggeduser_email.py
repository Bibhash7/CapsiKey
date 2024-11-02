# Generated by Django 5.1.2 on 2024-11-02 18:36

import constantClassApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("constantClassApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="loggeduser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="loggeduser",
            name="email",
            field=models.EmailField(
                max_length=254,
                unique=True,
                validators=[constantClassApp.models.custom_email_validator],
            ),
        ),
    ]
