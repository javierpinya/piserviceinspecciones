# Generated by Django 2.2.7 on 2020-01-15 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClaseModelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de alta')),
                ('edited_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición')),
                ('created_by', models.CharField(max_length=20, null=True)),
                ('edited_by', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('clasemodelo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='insp.ClaseModelo')),
                ('matricula', models.CharField(blank=True, max_length=10, null=True)),
                ('tara', models.IntegerField(blank=True, null=True)),
                ('peso_maximo', models.IntegerField(blank=True, null=True)),
                ('num_compartimentos', models.IntegerField(blank=True, null=True)),
                ('combustible', models.CharField(blank=True, max_length=14, null=True)),
                ('Fuel', models.BooleanField(blank=True, null=True)),
                ('gasoleo', models.BooleanField(blank=True, null=True)),
                ('marca', models.CharField(blank=True, max_length=20, null=True)),
                ('modelo', models.CharField(blank=True, max_length=20, null=True)),
                ('color', models.CharField(blank=True, max_length=15, null=True)),
                ('kilometros', models.PositiveIntegerField(blank=True, null=True)),
                ('bastidor', models.CharField(blank=True, max_length=25, null=True)),
                ('asegurado', models.BooleanField(blank=True, null=True)),
                ('aseguradora', models.CharField(blank=True, max_length=50, null=True)),
                ('libro_mto', models.BooleanField(blank=True, null=True)),
                ('num_poliza', models.CharField(blank=True, max_length=20, null=True)),
                ('tipo_motor', models.CharField(blank=True, max_length=50, null=True)),
                ('placa_oval', models.CharField(blank=True, max_length=15, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
            bases=('insp.clasemodelo',),
        ),
        migrations.CreateModel(
            name='Inspeccion',
            fields=[
                ('clasemodelo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='insp.ClaseModelo')),
                ('inspector', models.CharField(max_length=10)),
                ('itv', models.BooleanField(null=True)),
                ('adr', models.BooleanField(null=True)),
                ('ficha_seguridad', models.BooleanField(null=True)),
                ('tabla_calibracion', models.CharField(blank=True, max_length=40, null=True)),
                ('fecha_tabla_cal', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha tabla de calibracion')),
                ('chip', models.BooleanField(null=True)),
                ('SuperficieAntideslizante', models.BooleanField(null=True)),
                ('Apagallamas', models.BooleanField(null=True)),
                ('ConexionTomaTierra', models.BooleanField(null=True)),
                ('ConexiónMangueraGases', models.BooleanField(null=True)),
                ('BocasCompartimentosOk', models.BooleanField(null=True)),
                ('Apis', models.BooleanField(null=True)),
                ('EstanqueidadCisterna', models.BooleanField(null=True)),
                ('EstanqueidadValvulasApi', models.BooleanField(null=True)),
                ('EstanqueidadCajon', models.BooleanField(null=True)),
                ('MontajeTags', models.BooleanField(null=True)),
                ('LecturaTags', models.BooleanField(null=True)),
                ('Inspeccionada', models.BooleanField(null=True)),
                ('Favorable', models.BooleanField(null=True)),
                ('Revisada', models.BooleanField(null=True)),
                ('Bloqueada', models.BooleanField(null=True)),
                ('Versión', models.IntegerField(default=0)),
                ('matricula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insp.Vehiculo')),
            ],
            bases=('insp.clasemodelo',),
        ),
        migrations.CreateModel(
            name='Compartimentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacidad', models.IntegerField(blank=True, null=True)),
                ('altura_sonda', models.IntegerField(blank=True, null=True)),
                ('placa', models.IntegerField(blank=True, null=True)),
                ('cantidad_cargada', models.IntegerField(blank=True, null=True)),
                ('cantidad_96', models.IntegerField(blank=True, null=True)),
                ('diferencia', models.IntegerField(blank=True, null=True)),
                ('codigo_tag', models.IntegerField(blank=True, null=True)),
                ('matricula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insp.Vehiculo')),
            ],
        ),
    ]
