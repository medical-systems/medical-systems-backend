# Generated by Django 4.1.5 on 2023-08-28 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_treatments_appointmenttreatment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmenttreatment',
            old_name='appointment_id',
            new_name='appointment',
        ),
        migrations.RenameField(
            model_name='appointmenttreatment',
            old_name='treatment_id',
            new_name='treatment',
        ),
    ]