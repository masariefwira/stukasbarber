# Generated by Django 4.0.2 on 2022-09-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_layanan',
            name='id_detail_layanan',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='layanan',
            name='id_layanan',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='id_transaksi',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]