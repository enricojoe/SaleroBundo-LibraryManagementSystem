from django.forms import ModelForm
from .models import Subscribers, Borrowing

# Create your tests here.

class FormSubscriber(ModelForm):
	class Meta:
		model = Subscribers
		exclude = ['status']

class FormBorrowing(ModelForm):
	class Meta:
		model = Borrowing
		exclude = ['tgl_peminjaman','tgl_pengembalian', 'pembayaran', 'status', 'tgl_dikembalikan']