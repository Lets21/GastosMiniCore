from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL('DROP SCHEMA public CASCADE;'),
        migrations.RunSQL('CREATE SCHEMA public;'),
    ] 