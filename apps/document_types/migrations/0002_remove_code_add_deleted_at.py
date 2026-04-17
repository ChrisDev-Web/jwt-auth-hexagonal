from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("document_types", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="documenttypemodel",
            name="code",
        ),
        migrations.AddField(
            model_name="documenttypemodel",
            name="deleted_at",
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
