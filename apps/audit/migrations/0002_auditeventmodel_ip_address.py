from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("audit", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="auditeventmodel",
            name="ip_address",
            field=models.CharField(blank=True, db_index=True, default="", max_length=45),
        ),
    ]
