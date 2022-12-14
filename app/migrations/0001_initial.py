# Generated by Django 4.0.2 on 2022-09-19 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='layanan',
            fields=[
                ('id_layanan', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_layanan', models.CharField(max_length=50)),
                ('harga', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pelayan',
            fields=[
                ('id_pelayan', models.AutoField(primary_key=True, serialize=False)),
                ('nama_pelayan', models.CharField(max_length=50)),
                ('no_hp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transaksi',
            fields=[
                ('id_transaksi', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_pelanggan', models.CharField(max_length=50)),
                ('tanggal', models.DateField()),
                ('id_pelayan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pelayan')),
            ],
        ),
        migrations.CreateModel(
            name='detail_layanan',
            fields=[
                ('id_detail_layanan', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('id_layanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.layanan')),
                ('id_transaksi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.transaksi')),
            ],
        ),
    ]
