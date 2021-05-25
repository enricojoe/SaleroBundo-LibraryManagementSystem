# Generated by Django 2.2.10 on 2021-05-25 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('item_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('jenis', models.CharField(editable=False, max_length=20)),
                ('judul', models.CharField(max_length=20)),
                ('thumbnail', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Perpustakaan',
            fields=[
                ('id_perpustakaan', models.AutoField(primary_key=True, serialize=False)),
                ('nama_perpustakaan', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Perpustakaan',
            },
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id_subscriber', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('tingkat_member', models.CharField(choices=[('Regular', 'Regular'), ('Golden', 'Golden')], max_length=10)),
                ('nama_peminjam', models.CharField(max_length=20, verbose_name='Nama')),
                ('alamat_peminjam', models.CharField(max_length=50, verbose_name='Alamat')),
                ('phone_peminjam', models.CharField(max_length=14, verbose_name='No Telephone')),
                ('email_peminjam', models.EmailField(max_length=50, verbose_name='Email')),
                ('status', models.BooleanField(default=False, verbose_name='Disetujui')),
            ],
            options={
                'verbose_name_plural': 'Subscribers',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('items_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='perpus.items')),
                ('penulis', models.CharField(max_length=20)),
                ('penerbit', models.CharField(max_length=20)),
                ('tahun_terbit', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Article',
            },
            bases=('perpus.items',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('items_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='perpus.items')),
                ('penulis', models.CharField(max_length=20)),
                ('penerbit', models.CharField(max_length=20)),
                ('tahun_terbit', models.PositiveIntegerField()),
                ('salinan', models.PositiveIntegerField(verbose_name='salinan (/copy)')),
            ],
            options={
                'verbose_name_plural': 'Book',
            },
            bases=('perpus.items',),
        ),
        migrations.CreateModel(
            name='DigitalMedia',
            fields=[
                ('items_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='perpus.items')),
            ],
            bases=('perpus.items',),
        ),
        migrations.AddField(
            model_name='items',
            name='id_perpustakaan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='perpus.Perpustakaan'),
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_peminjaman', models.DateTimeField()),
                ('tgl_pengembalian', models.DateTimeField(editable=False)),
                ('pembayaran', models.CharField(editable=False, max_length=20)),
                ('id_subscriber', models.ForeignKey(max_length=8, null=True, on_delete=django.db.models.deletion.SET_NULL, to='perpus.Subscribers')),
                ('item_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='perpus.items')),
            ],
            options={
                'verbose_name_plural': 'Borrowing',
            },
        ),
    ]