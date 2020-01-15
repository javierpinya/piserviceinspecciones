from django.db import models

class ClaseModelo(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta', null=True)
	edited_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición', null=True)
	created_by = models.CharField(max_length=20,null=True)
	edited_by = models.CharField(max_length=20,null=True)

class Vehiculo(ClaseModelo):
	matricula = models.CharField(max_length=10,null=True, blank=True)
	tara = models.IntegerField(null=True,blank=True)
	peso_maximo = models.IntegerField(null=True,blank=True)
	num_compartimentos = models.IntegerField(null=True,blank=True)
	combustible = models.CharField(max_length=14,null=True,blank=True)
	Fuel = models.BooleanField(null=True,blank=True)
	gasoleo=models.BooleanField(null=True,blank=True)
	marca = models.CharField(max_length=20, null=True, blank=True)
	modelo = models.CharField(max_length=20, null=True, blank=True)
	color = models.CharField(max_length=15, null=True, blank=True)
	kilometros = models.PositiveIntegerField(null=True, blank=True)
	bastidor = models.CharField(max_length=25, null=True, blank=True)
	asegurado = models.BooleanField(null=True, blank=True)
	aseguradora =models.CharField(max_length=50, null=True, blank=True)
	libro_mto = models.BooleanField(null=True, blank=True)
	num_poliza = models.CharField(max_length=20, null=True, blank=True)
	tipo_motor = models.CharField(max_length=50, null=True, blank=True)
	placa_oval = models.CharField(max_length=15, null=True, blank=True)
	observaciones = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.matricula

class Inspeccion(ClaseModelo):
	matricula = models.ForeignKey(Vehiculo,null=True,on_delete=models.CASCADE)
	inspector = models.CharField(max_length=10)
	itv = models.BooleanField(null=True)
	adr = models.BooleanField(null=True)
	ficha_seguridad = models.BooleanField(null=True)
	tabla_calibracion = models.CharField(max_length=40,null=True,blank=True)
	fecha_tabla_cal = models.DateTimeField(auto_now_add=True,null=True,blank=True,verbose_name='Fecha tabla de calibracion')
	chip = models.BooleanField(null=True) #Transponder
	SuperficieAntideslizante = models.BooleanField(null=True)
	Apagallamas = models.BooleanField(null=True)
	ConexionTomaTierra = models.BooleanField(null=True)
	ConexiónMangueraGases = models.BooleanField(null=True)
	BocasCompartimentosOk = models.BooleanField(null=True)
	Apis = models.BooleanField(null=True)
	EstanqueidadCisterna = models.BooleanField(null=True)
	EstanqueidadValvulasApi = models.BooleanField(null=True)
	EstanqueidadCajon = models.BooleanField(null=True)
	MontajeTags = models.BooleanField(null=True)
	LecturaTags = models.BooleanField(null=True)
	Inspeccionada = models.BooleanField(null=True)
	Favorable = models.BooleanField(null=True)
	Revisada = models.BooleanField(null=True)
	Bloqueada = models.BooleanField(null=True)
	Versión = models.IntegerField(default=0)

class Compartimentos(models.Model):
	matricula = models.ForeignKey(Vehiculo,null=True,on_delete=models.CASCADE)
	capacidad=models.IntegerField(null=True,blank=True)
	altura_sonda=models.IntegerField(null=True,blank=True)
	placa=models.IntegerField(null=True,blank=True)
	cantidad_cargada=models.IntegerField(null=True,blank=True)
	cantidad_96=models.IntegerField(null=True,blank=True)
	diferencia=models.IntegerField(null=True,blank=True)
	codigo_tag=models.IntegerField(null=True,blank=True)









