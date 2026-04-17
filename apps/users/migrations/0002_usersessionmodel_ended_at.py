from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersessionmodel",
            name="ended_at",
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
