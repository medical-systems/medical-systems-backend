# Generated by Django 4.1.5 on 2023-09-03 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_alter_appointment_doctor_alter_appointment_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_name', models.CharField(blank=True, default=' ', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='treatment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointments.treatment'),
        ),
    ]
