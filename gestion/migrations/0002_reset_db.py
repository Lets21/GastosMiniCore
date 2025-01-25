from django.db import migrations

def reset_db(apps, schema_editor):
    # Obtener los modelos
    Gasto = apps.get_model('gestion', 'Gasto')
    Empleado = apps.get_model('gestion', 'Empleado')
    Departamento = apps.get_model('gestion', 'Departamento')
    
    # Limpiar datos existentes
    Gasto.objects.all().delete()
    Empleado.objects.all().delete()
    Departamento.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(reset_db),
    ] 