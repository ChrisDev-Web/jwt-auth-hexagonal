import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0002_usersessionmodel_ended_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuditEventModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("action", models.CharField(choices=[("LOGIN", "LOGIN"), ("LOGOUT", "LOGOUT"), ("REGISTER", "REGISTER"), ("CREATE", "CREATE"), ("UPDATE", "UPDATE"), ("DELETE", "DELETE")], db_index=True, max_length=20)),
                ("message", models.CharField(max_length=255)),
                ("entity_type", models.CharField(blank=True, default="", max_length=100)),
                ("entity_id", models.PositiveBigIntegerField(blank=True, null=True)),
                ("entity_name", models.CharField(blank=True, default="", max_length=150)),
                ("session_state", models.CharField(blank=True, choices=[("ACTIVE", "ACTIVE"), ("INACTIVE", "INACTIVE")], default="", max_length=10)),
                ("session_started_at", models.DateTimeField(blank=True, null=True)),
                ("session_ended_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("user", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={"db_table": "audit_events"},
        ),
    ]
