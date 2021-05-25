from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import items, Borrowing
from .forms import FormSubscriber, FormBorrowing
from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from .utils import render_to_pdf
# import pywkhtmltopdf as pdf

# from weasyprint import HTML

# Create your views here.
def index(request):
	context = {}
	html_template = loader.get_template( 'index.html' )
	return HttpResponse(html_template.render(context, request))

def page(request):
	context = {}
	html_template = loader.get_template( 'daftar_buku.html' )
	return HttpResponse(html_template.render(context, request))

# def page(request):
# 	context = {}
# 	html_template = loader.get_template( 'daftar_buku.html' )
# 	return HttpResponse(html_template.render(context, request))

def cari_buku(request):
	# print(request.method)
	if request.method == 'POST': 
		cari = request.POST['cari_item']
		hasil = items.objects.filter(judul__contains=cari)
		context = {}
		context['hasil_cari'] = hasil
		html_template = loader.get_template( 'cari_buku.html' )
		return HttpResponse(html_template.render(context, request))
	html_template = loader.get_template( 'cari_buku.html' )
	return HttpResponse(html_template.render({}, request))

def pendaftaran(request):
	berhasil = False
	if request.method == "POST":
		form = FormSubscriber(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/pendaftaran?berhasil=True')
	else:
		form = FormSubscriber
		if 'berhasil' in request.GET:
			berhasil = True
	context = {
		'form':form,
		'berhasil':berhasil
	}
	html_template = loader.get_template( 'pendaftaran.html' )
	return HttpResponse(html_template.render(context, request))

def detail_item(request,pk):
	item = get_object_or_404(items,pk = pk)
	form = FormBorrowing(request.POST)
	berhasil = False
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/item/%s?berhasil=True'%pk)
	else:
		form = FormBorrowing
		if 'berhasil' in request.GET:
			berhasil = True
	context = {
		'item':item,
		'form':form,
		'berhasil':berhasil
	}
	html_template = loader.get_template( 'detail_item.html' )
	return HttpResponse(html_template.render(context, request))


# def cetak(request):
#     laporan=Borrowing.objects.all()
#     context = {
#         "peminjaman":peminjaman
#     }
#     pdf = render_to_pdf('pengembalian.html', all)
#     return HttpResponse(pdf, content_type='application/pdf')


def cetak(request):
    
    peminjaman = Borrowing.objects.all()
    context = {
    	'peminjaman':peminjaman
    } # something
    pdf = render_to_pdf('pengembalian.html', context)
    return HttpResponse(pdf, content_type='application/pdf')
    # html_string = render_to_string('pengembalian.html',context)
    # html = HTML(string=html_string, base_url=request.build_absolute_uri())
    # html.write_pdf(target='/tmp/laporan.pdf');
    # fs = FileSystemStorage('/tmp')
    # with fs.open('laporan.pdf') as pdf:
    #     response = HttpResponse(pdf, content_type='application/pdf')
    #     response['Content-Disposition'] = 'filename=Report.pdf'
    #     return response
    # return response
# class DetailBuku(DetailView):
# 	html_template = loader.get_template( 'detail_buku.html' )
# 	def get_object(self):
# 		return get_object_or_404(items, )


# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:
        
#         load_template      = request.path.split('/')[-1]
#         context = {}
        
#         html_template = loader.get_template( load_template )
#         return HttpResponse(html_template.render(context, request))
        
#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template( 'page-404.html' )
#         return HttpResponse(html_template.render(context, request))

#     except:
    
#         html_template = loader.get_template( 'page-500.html' )
#         return HttpResponse(html_template.render(context, request))
