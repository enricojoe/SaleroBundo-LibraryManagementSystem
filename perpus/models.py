from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class Perpustakaan(models.Model):
	id_perpustakaan = models.AutoField(primary_key = True)
	nama_perpustakaan = models.CharField(max_length = 20)
	def __str__(self):
		return str(self.nama_perpustakaan)
	class Meta:
		verbose_name_plural = 'Perpustakaan'

class items(models.Model):
	item_id = models.CharField(primary_key = True, max_length = 8)
	id_perpustakaan = models.ForeignKey('Perpustakaan',on_delete = models.SET_NULL, null = True)
	jenis = models.CharField(max_length = 20, editable = False)
	judul = models.CharField(max_length = 20)
	thumbnail = models.ImageField(null = True)
	def __str__(self):
		return self.judul

class Subscribers(models.Model):
	id_subscriber = models.CharField(primary_key = True, max_length = 8)
	TIPE = {
		('Regular', 'Regular'),
		('Golden', 'Golden')
	}
	tingkat_member = models.CharField(max_length = 10, choices = TIPE)
	nama_peminjam = models.CharField(max_length = 20, verbose_name = 'Nama')
	alamat_peminjam = models.CharField(max_length = 50, verbose_name = 'Alamat')
	phone_peminjam = models.CharField(max_length = 14,verbose_name = 'No Telephone')
	email_peminjam = models.EmailField(max_length = 50, verbose_name = 'Email')
	status = models.BooleanField(default = False, verbose_name = 'Disetujui')
	def __str__(self):
		return str(self.nama_peminjam)
	class Meta:
		verbose_name_plural = 'Subscribers'

class Borrowing(models.Model):
	id_subscriber = models.ForeignKey('Subscribers', max_length = 8, on_delete = models.SET_NULL, null = True)
	tgl_peminjaman = models.DateTimeField(editable = False, null = True)
	item_id = models.ForeignKey('items', on_delete = models.SET_NULL, null = True)
	tgl_pengembalian = models.DateTimeField(editable = False, null = True)
	tgl_dikembalikan = models.DateTimeField(null = True)
	pembayaran = models.CharField(max_length = 20, editable = False)
	status = models.BooleanField(default = False, verbose_name = 'Dikembalikan')
	def save(self, *args, **kwargs):
		if str(Subscribers.objects.get(nama_peminjam = self.id_subscriber).tingkat_member) == 'Regular':
			# if self.tgl_pengembalian > self.tgl_peminjaman + timedelta(days = 21):
			# 	denda = self.tgl_pengembalian - self.tgl_peminjaman + timedelta(days = 21)
			# 	biaya = (denda // 7)*5000
			# 	self.pembayaran = biaya
			self.tgl_peminjaman = datetime.now()
			self.tgl_pengembalian = self.tgl_peminjaman + timedelta(21)
				
		else:
			# if self.tgl_pengembalian > self.tgl_peminjaman + timedelta(days = 90):
			# 	denda = self.tgl_pengembalian - self.tgl_peminjaman + timedelta(days = 90)
			# 	biaya = (denda // 7)*5000
			# 	self.pembayaran = biaya
			self.tgl_peminjaman = datetime.now()
			self.tgl_pengembalian = self.tgl_peminjaman + timedelta(21)

		super(Borrowing, self).save(*args, **kwargs)
	def __str__(self):
		return str(self.id_subscriber)
	class Meta:
		verbose_name_plural = 'Borrowing'

class Book(items):
	# models.CharField(max_length = 20, default = 'Book', editable = False)
	jenis = 'Book'
	penulis = models.CharField(max_length = 20)
	penerbit = models.CharField(max_length = 20)
	tahun_terbit = models.PositiveIntegerField()
	salinan = models.PositiveIntegerField(verbose_name = 'salinan (/copy)')
	class Meta:
		verbose_name_plural = 'Book'

class Article(items):
	jenis = 'Article'
	penulis = models.CharField(max_length = 20)
	penerbit = models.CharField(max_length = 20)
	tahun_terbit = models.PositiveIntegerField()
	class Meta:
		verbose_name_plural = 'Article'

class DigitalMedia(items):
	jenis = 'Digital Media'
	class Meta:
		verbose_name_plural = 'Digital Media'