# Generated by Django 2.1.5 on 2019-01-29 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Repositorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fechaCreacion', models.DateTimeField(default=None)),
                ('fechaCommit', models.DateTimeField(default=None)),
                ('consultaApi', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='miapppy.ConsultaAPI')),
            ],
        ),
    ]
