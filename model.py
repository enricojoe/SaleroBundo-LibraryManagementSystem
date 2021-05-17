from perpus.db import models
from perpus import froms

class Perpustakaan(models.Model):
		id = models.AutoField(primary_key = True)
		Nama = models.CharField(max_length = 20)
		def __str__(self):
			return str(self.nama)
		class Meta:
			verbose_name_plural = 'Perpustakaan'

class items(models.Model):
		item_id = models.CharField(primary_key = True)
		Library_id = models.CharField(max_length = 5)
		jenis = models.CharField(max_length = 20)
		judul = models.CharField(max_length = 20)
		penulis = models.CharField(max_length = 20)
		penerbit = models.CharField(max_length = 20)
		tahun_terbit = models.PositiveIntegerField(max_length = 4)
		salinan = models.PositiveIntegerField(verbose_name = 'salinan (/copy)')
		def __str__(self):
			return self.judul
		class Meta:
			verbose_name_plural = 'items'

class Subcribers(models.Model):
	id = models.CharField(primary_key = True)
	tingkat_member = models.CharField(max_length = 10)
	nama_peminjam = models.CharField(max_length = 20)
	alamat_peminjam = models.CharField(max_length = 50)
	phone_peminjam = models.PositiveIntegerField(max_length = 15)
	email_peminjam = models.CharField(max_length = 50)
	def __str__(self):
		return self.nama_peminjam
	class Meta:
		verbose_name_plural = 'Subcribers'

class Borrowing(models.Model):
	id_subscriber = models.CharField(primary_key = True)
	tgl_peminjaman = models.DateTimeField()
	content_id = models.CharField(max_length = 20)
	tgl_pengembalian = models.DateTimeField()
	pembayaran = models.CharField(max_length = 20)
	def __str__(self):
		return self.id_subscriber
	class Meta:
		verbose_name_plural = 'Borrowing'



