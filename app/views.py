from datetime import datetime
from unittest import result
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import models
from django.template.loader import render_to_string
import tempfile
from django.db.models import Sum
import os
from weasyprint import HTML



# Create your views here.
def home (request):
  layanan_obj = models.layanan.objects.all()
  return render(request,'home.html',{
    'layanan': layanan_obj
  })


def pelayan(request):
  pelayan_obj = models.pelayan.objects.all()
  return render(request,'pelayan.html',{
  'pelayan': pelayan_obj
  })

def add_pelayan(request):
  if request.method == "GET":
    return render(request,'addpelayan.html')
  else:
    nama_pelayan = request.POST['nama_pelayan']
    no_hp = request.POST['no_hp']
    # jumlah_pelayan = models.pelayan.objects.all().last()
    # total_len = len(str(jumlah_pelayan))
    # if total_len == 1:
    #   id_pelayan = 'P_00'+str(jumlah_pelayan+1)
    # else:
    #   id_pelayan = 'P_00'+str(jumlah_pelayan+1)

  new_pelayan = models.pelayan(
    # id_pelayan = id_pelayan,
    nama_pelayan = nama_pelayan,
    no_hp = no_hp
  )
  new_pelayan.save()

  return redirect ('pelayan')

def update_pelayan(request,id):
  pelayan_obj = models.pelayan.objects.get(id_pelayan = id)
  if request.method == "GET":
    return render(request, 'updatepelayan.html',{
      'pelayan': pelayan_obj,
    })
  else:
    pelayan_obj.nama_pelayan = request.POST['nama_pelayan']
    pelayan_obj.no_hp = request.POST['no_hp']
    pelayan_obj.save()
    return redirect('pelayan')

def delete_pelayan(request,id):
  pelayan_obj = models.pelayan.objects.get(id_pelayan=id)
  pelayan_obj.delete()
  return redirect ('pelayan')

def layanan (request):
  layanan_obj = models.layanan.objects.all()
  return render(request,'layanan.html',{
    'layanan': layanan_obj
  })

def add_layanan(request):
  if request.method == "GET":
    return render(request,'addlayanan.html')
  else:
    nama_layanan = request.POST['nama_layanan']
    harga = request.POST['harga']
    # jumlah_layanan = models.layanan.objects.all().count()
    # total_len = len(str(jumlah_layanan))
    # if total_len == 1:
    #   id_layanan = 'L_00'+str(jumlah_layanan+1)
    # else:
    #   id_layanan = 'L_00'+str(jumlah_layanan+1)

    new_layanan = models.layanan(
      # id_layanan=id_layanan,
      nama_layanan = nama_layanan,
      harga = harga
    )
    new_layanan.save()
    return redirect('home')

def update_layanan(request,id):
  layanan_obj = models.layanan.objects.get(id_layanan = id)
  if request.method == "GET":
    return render(request,"updatelayanan.html",{
      'layanan' : layanan_obj
    })
  else:
    layanan_obj.nama_layanan=request.POST['nama_layanan']
    layanan_obj.harga=request.POST['harga']
    layanan_obj.save()
    return redirect('home')
    
def delete_layanan(request,id):
  layanan_obj = models.layanan.objects.get(id_layanan=id)
  layanan_obj.delete()
  return redirect ('home')

def transaksi (request):
  data=[]
  transaksi_obj = models.transaksi.objects.all()
  print(transaksi_obj)
  print('aaaaa')
  for item in transaksi_obj:
    dummy=[]
    print(item)
    idtransaksi = item.id_transaksi
    # Get Specific detail layanan by item 
    specificdetail = models.detail_layanan.objects.filter(id_transaksi = idtransaksi)
    dummy.append(item)
    dummy.append(specificdetail)
    data.append(dummy)
  print(data[0][1])
  return render(request,'transaksi.html',{
    'transaksi': data,
  })

def add_transaksi(request):
  pelayan_obj = models.pelayan.objects.all()
  layanan_obj = models.layanan.objects.all()

  if request.method == "GET":
    return render (request,'addtransaksi.html',{
            'pelayan' : pelayan_obj,
            'layanan' : layanan_obj
            })
  else:
    print(request.POST)
    idpelayan = request.POST['nama_pelayan']
    getpelayanbaru = models.pelayan.objects.get(id_pelayan = idpelayan)
    idlayanan = request.POST['nama_layanan']
    getlayananbaru = models.layanan.objects.get(id_layanan = idlayanan)
    pelayan_obj = getpelayanbaru
    layanan_obj = getlayananbaru
    nama_pelanggan = request.POST['nama_pelanggan']
    tanggal = request.POST['tanggal']
    
    
    new_transaksi = models.transaksi(
      # id_transaksi = id_transaksi,
      id_pelayan = pelayan_obj,
      nama_pelanggan=nama_pelanggan,
      tanggal = tanggal
    )
    new_transaksi.save()

    
    #tambah id detail layanan
    transaksi_obj = models.transaksi.objects.all().last()
    
    
    # add pemesanan to database
    new_detail_layanan = models.detail_layanan(
        # id_detail_layanan = id_detail_layanan,
        id_transaksi = transaksi_obj,
        id_layanan = layanan_obj,
    )
    new_detail_layanan.save()
    return redirect ('transaksi')
  
def update_transaksi (request,id):
  ''' salahnya di pelaan obj karena parameter id isinya adalah id transaksi bukan id pelayan
      makannya pas di get di pelayan_obj dia error karena gaada id pelayan dengan id yg sesuai.
  '''
  # pelayan_obj = models.pelayan.objects.get(id_pelayan = id)
  transaksi_obj = models.transaksi.objects.get(id_transaksi=id)
  layanan_obj = models.layanan.objects.all()
  # Alternatif solusi
  pelayan_obj = models.pelayan.objects.get(id_pelayan = transaksi_obj.id_pelayan_id)
  ''' Bisa di get dulu transaksi objnya karena parameter id yg dikirim adalah id transaksi. karena transaksi berelasi dengan entitas pelayan
      maka bisa diambil id pelayan dari entitas transaksi dengan cara panggil objeknya terus akses atributnya contoh :
      transaksi_obj.id_pelayanan_id --> cara bacanya dari objek transaksi_obj panggil atribut id_pelayanan_id. id_pelayanan_id didapat dari 
      field di database. bisa disesuaikan buat nama fieldnya
  '''
  pelayanall = models.pelayan.objects.all()
  tanggal = datetime.strftime(transaksi_obj.tanggal, '%Y-%m-%d')
  if request.method =="GET":
    return render(request,'updatetransaksi.html',{
      'transaksi' : transaksi_obj,
      'layanan' : layanan_obj,
      # Jangan lupa karena pelayan_obj ini diambil dari metode get maka tidak perlu di for loop untuk pengaksesan tiap atributnya. 
      # Dapat langsung dipanggil berdasarkan atributnya
      'pelayan' : pelayanall,
      'tanggal' : tanggal
    })
  else:
    transaksi_obj.nama_pelanggan = request.POST['nama_pelanggan']
    getlayananbaru = models.layanan.objects.get(id_layanan = request.POST['nama_layanan'])
    transaksi_obj.id_layanan = getlayananbaru
    transaksi_obj.tanggal = request.POST['tanggal']
    getpelayanbaru = models.pelayan.objects.get(id_pelayan = request.POST['nama_pelayan'])
    transaksi_obj.id_pelayan= getpelayanbaru
    transaksi_obj.save()
    return redirect('transaksi')
  
def delete_transaksi (request,id):
  transaksi_obj = models.transaksi.objects.get(id_transaksi=id)
  transaksi_obj.delete()
  return redirect ('transaksi')

def detail_layanan (request,id):
  detail_layanan_obj = models.detail_layanan.objects.filter(id_transaksi = id)
  return render(request,'detaillayanan.html',{
        'detail_layanan':detail_layanan_obj
    })

def update_detail_layanan(request,id):
  detail_layanan_obj = models.detail_layanan.objects.get(id_detail_layanan = id)
  layanan_obj = models.layanan.objects.all()
  if request.method == "GET":
    return render(request,"updatedetaillayanan.html",{
      'detaillayanan' : detail_layanan_obj,
      'layanan' : layanan_obj
    })
  else:
    id_layanan = request.POST['id_layanan']
    layananobj = models.layanan.objects.get(id_layanan=id_layanan)
    detail_layanan_obj.id_layanan = layananobj
    detail_layanan_obj.save()
    return redirect('transaksi')

def delete_detail_layanan (request,id):
  detail_layanan_obj = models.detail_layanan.objects.get(id_detail_layanan = id)
  detail_layanan_obj.delete()
  return redirect ('transaksi')

def add_detail_layanan(request):
  transaksi_obj = models.transaksi.objects.all()
  layanan_obj = models.layanan.objects.all()
  if request.method == "GET":
    return render(request,'adddetaillayanan.html',{
    'layanan': layanan_obj,
    'transaksi': transaksi_obj
  })

  else:
    idtransaksi = request.POST['id_transaksi']
    gettransaksibaru = models.transaksi.objects.get(id_transaksi = idtransaksi)
    idlayanan = request.POST['nama_layanan']
    getlayananbaru = models.layanan.objects.get(id_layanan = idlayanan)
    transaksi_obj = gettransaksibaru
    layanan_obj = getlayananbaru

    new_detail_layanan = models.detail_layanan(
      id_layanan=layanan_obj,
      id_transaksi=transaksi_obj
      
    )
    new_detail_layanan.save()
    return redirect('transaksi')

def laporan(request):
  if request.method == "GET":
    return render(request, 'laporan.html')
  elif request.method == "POST":
    mulai = request.POST ['mulai']
    akhir = request.POST ['akhir']
    transaksi_obj = models.transaksi.objects.filter(tanggalsewa__range=(mulai,akhir))
    for item in transaksi_obj:
      data=[]
      detail_layanan_obj = models.detail_layanan.objects.filter(id_transaksi = item.id_transaksi)
      data.append(item)
      data.append(detail_layanan_obj)
      totallayanan = detail_layanan_obj.aggregate(Sum('hargalayanan'))
      

def notapdf(request,id):
    # Get selected object 
    # layanan_obj = models.layanan.objects.get(id_layanan = id)
    # Get Detail penyewaan
    transaksi_obj = models.transaksi.objects.get(id_transaksi = id)
    pelayan_obj = models.pelayan.objects.filter(id_pelayan = transaksi_obj.id_pelayan.id_pelayan)
    # Get detail layanan
    detaillayananobj = models.detail_layanan.objects.filter(id_transaksi = id)
    # total layanan
    # totallayanan = transaksi_obj.aggregate(Sum('harga'))
    # totallayanan = totallayanan['harga__sum']
    layananobjplus = []
    for i in range(len(detaillayananobj)):
      layananobj = models.layanan.objects.filter(id_layanan = detaillayananobj[i].id_layanan.id_layanan)
      totallayanantes = layananobj.aggregate(Sum('harga'))
      print(totallayanantes,'ini total layanan tes')
      totallayanantesvalue = totallayanantes['harga__sum']
      layananobjplus.append(totallayanantesvalue)
    print(layananobjplus,'ini layanan obj plus')
    
    # total charge
    totallayanan1 = sum(layananobjplus)
    print(layananobj,'ini layanan obj')
    print(detaillayananobj,'ini detail layanan obj')
    print(detaillayananobj[0],'ini detail layanan obj')
    print(totallayanan1)
    totallayanan = int(totallayanan1)

    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_of_students.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    html_string = render_to_string(
        'notapdf.html',{
            'transaksi' : transaksi_obj,
            'pelayan' :pelayan_obj,
            'detail_layanan' : detaillayananobj,
            'totallayanan' : totallayanan
            
            }
    )
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.seek(0)
        response.write(output.read())
    
    return response


def laporan(request):
    if request.method == "GET":
        return render(request,'laporan.html')
    elif request.method == "POST":
        detailobj =[]
        listharga=[]
        
        # Get selected penyewaan object
        mulai = request.POST['mulai']
        akhir = request.POST['akhir']
        transaksiobj = models.transaksi.objects.filter(tanggal__range=(mulai,akhir))
        for item in transaksiobj:
          lol =[]
          # Get filtered detail layanan
          transaksiobj2 = models.transaksi.objects.filter(id_transaksi = item.id_transaksi)
          detaillayananobj = models.detail_layanan.objects.filter(id_transaksi = item.id_transaksi)
          lol.append(transaksiobj2)
          lol.append(detaillayananobj)
          detailobj.append(lol)
          print(detaillayananobj)
          for i in detaillayananobj:
            harga = i.id_layanan.harga
            listharga.append(harga)


        print(listharga, 'wow')
        totalharga = sum(listharga)
        print(totalharga)

        print(detailobj)
        for i in detailobj:
          print(i)
    

        return render(request,'detaillaporan.html',{
            'detailobjek' :detailobj,
            'hargalayanan':listharga,
            'tanggalmulai' : mulai,
            'tanggalakhir' : akhir,
            'totalharga' : totalharga

        })


def laporanpdf(request,mulai,akhir):
    
        detailobj =[]
        listharga=[]
      
        transaksiobj = models.transaksi.objects.filter(tanggal__range=(mulai,akhir))
        for item in transaksiobj:
          lol =[]
          # Get filtered detail layanan
          transaksiobj2 = models.transaksi.objects.filter(id_transaksi = item.id_transaksi)
          detaillayananobj = models.detail_layanan.objects.filter(id_transaksi = item.id_transaksi)
          lol.append(transaksiobj2)
          lol.append(detaillayananobj)
          detailobj.append(lol)
          print(detaillayananobj)
          for i in detaillayananobj:
            harga = i.id_layanan.harga
            listharga.append(harga)


        print(listharga, 'wow')
        totalharga = sum(listharga)
        print(totalharga)

        print(detailobj)
        for i in detailobj:
          print(i)
    

        

        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename=list_of_students.pdf'
        response['Content-Transfer-Encoding'] = 'binary'
        html_string = render_to_string(
            'laporanpdf.html',{
              'detailobjek' :detailobj,
              'hargalayanan':listharga,
              'tanggalmulai' : mulai,
              'tanggalakhir' : akhir,
              'totalharga' : totalharga
                })
        html = HTML(string=html_string)
        result = html.write_pdf()

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output.seek(0)
            response.write(output.read())
        
        render(request,'laporanpdf.html')
        
        return response