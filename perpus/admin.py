from django.contrib import admin
from .models import Perpustakaan, Subscribers, Borrowing, Book, Article, DigitalMedia
# Register your models here.

class ListPerpustakaan(admin.ModelAdmin):
	list_display = ('nama_perpustakaan',)
admin.site.register(Perpustakaan, ListPerpustakaan)

class ListBook(admin.ModelAdmin):
	list_display = ('judul', 'penulis', 'penerbit', 'tahun_terbit', 'salinan')
admin.site.register(Book, ListBook)

class ListArticle(admin.ModelAdmin):
	list_display = ('judul', 'penulis', 'penerbit', 'tahun_terbit')
admin.site.register(Article, ListArticle)

class ListDigitalMedia(admin.ModelAdmin):
	list_display = ('judul',)
admin.site.register(DigitalMedia, ListDigitalMedia)

class ListSubscribers(admin.ModelAdmin):
	list_display = ('id_subscriber', 'nama_peminjam', 'tingkat_member', 'status')
admin.site.register(Subscribers, ListSubscribers)

class ListBorrowing(admin.ModelAdmin):
	list_display = ('id_subscriber', 'item_id', 'tgl_peminjaman', 'tgl_pengembalian', 'status')
admin.site.register(Borrowing, ListBorrowing)