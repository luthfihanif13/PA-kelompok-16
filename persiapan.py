#Program Ojekonline syariah
import time 
import sys
harga_km = 0
slogin = 0
ojek = {
	'penjemputan': ['SENTOSA', 'GAJAH MADA', 'PRAMUKA', 'PERJUANGAN', 'BENGKURING', 'PALARAN', 'JUANDA', 'CENDANA', 'ALAYA', 'LEMPAKE', 'REMAJA', 'PAHLAWAN', 'MAKROMAN', 'KEBAKTIAN', 'AWANG LONG', 'PEMUDA'],
	'tujuan': ['SENTOSA', 'GAJAH MADA', 'PRAMUKA', 'PERJUANGAN', 'BENGKURING', 'PALARAN', 'JUANDA', 'CENDANA', 'ALAYA', 'LEMPAKE', 'REMAJA', 'PAHLAWAN', 'MAKROMAN', 'KEBAKTIAN', 'AWANG LONG', 'PEMUDA'],
	'ikhwan': ['ADAM', 'BUDI', 'KAKA', 'RAHMAN', 'RASYID'],
	'akhwat': ['PUPUT', 'BILA', 'AMEL', 'RARA', 'EKA']
}

def list_jalanan(status):
  if status == True :
    for i in range (len(ojek['penjemputan'])):
      print(ojek['penjemputan'][i])
  else :
    for i in range (len(ojek['tujuan'])):
      print(ojek['tujuan'][i])

def tambah(status):
  if status == True :
    while True:
      tambahjalan=str(input("Masukkan Nama Jalan : ", ))
      if all(x.isalpha() or x.isspace() for x in tambahjalan):
        ojek['penjemputan'].append(tambahjalan.upper())
        time.sleep(2)
        break
      else :
        print ("Input dengan benar")
        continue
    
  else :
    while True:
      tambahjalan=str(input("Masukkan Nama Jalan : ", ))
      if all(x.isalpha() or x.isspace() for x in tambahjalan):
        ojek['tujuan'].append(tambahjalan.upper())
        time.sleep(2)
        break
      else :
        print ("Input dengan benar")
        continue

def update(status):
  if status == True :
    while True:
      updatejalan=str(input("Masukkan Nama Jalan Yang Ingin di Update : ", ))
      if all(x.isalpha() or x.isspace() for x in updatejalan):
        updatejalan = updatejalan.upper()
        if updatejalan in ojek['penjemputan']:
          index = ojek['penjemputan'].index(updatejalan)
          break
        else :
          print ("Nama Jalan Tidak Ada")
          continue 
      else :
        print ("Inputan Tidak boleh Selain Huruf")
        continue

    while True:
      updatejalan=str(input("Masukkan Nama Jalan : ", ))
      updatejalan = updatejalan.upper()
      if all(x.isalpha() or x.isspace() for x in updatejalan):
        ojek['penjemputan'][index] = updatejalan.upper()
        time.sleep(2)
        break
      else :
        print ("Input dengan benar")
        continue

  else :
    while True:
      carijalan=str(input("Masukkan Nama Jalan Yang Ingin di Update : ", ))
      if all(x.isalpha() or x.isspace() for x in carijalan):
        carijalan = carijalan.upper()
        if carijalan in ojek['tujuan']:
          index = ojek['tujuan'].index(carijalan)
          break
        else :
          print ("Nama Jalan Tidak Ada")
          continue
      else :
        print ("Inputan Tidak boleh Selain Huruf")
        continue

    while True:
      updatejalan=str(input("Masukkan Nama Jalan : ", ))
      if all(x.isalpha() or x.isspace() for x in updatejalan):
        ojek['tujuan'][index] = updatejalan.upper()
        time.sleep(2)
        break
      else :
        print ("Input dengan benar")
        continue

def hapus(status):
  if status == True :
    while True:
      carijalan=str(input("Masukkan Nama Jalan Yang Ingin di Hapus : ", ))
      carijalan = carijalan.upper()
      if all(x.isalpha() or x.isspace() for x in carijalan):
        index = ojek['penjemputan'].index(carijalan)
        ojek['penjemputan'].pop(index)
        time.sleep(2)
        break
      else :
        print ("Input dengan benar")
        continue

  else :
    while True:
      carijalan=str(input("Masukkan Nama Jalan Yang Ingin di Hapus : ", ))
      carijalan = carijalan.upper()
      if all(x.isalpha() or x.isspace() for x in carijalan):
        index = ojek['tujuan'].index(carijalan)
        ojek['tujuan'].pop(index)
        time.sleep(2)
        break
      else :
        print ("Input dengan benar")
        continue

def menuju():
    for i in range (15):
        sys.stdout.write('\rSedang menuju Lokasi penjemputan |')
        time.sleep(0.1)
        sys.stdout.write('\rSedang menuju Lokasi penjemputan /')
        time.sleep(0.1)
        sys.stdout.write('\rSedang menuju Lokasi penjemputan -')
        time.sleep(0.1)
        sys.stdout.write('\rSedang menuju Lokasi penjemputan \\')
        time.sleep(0.1)
    sys.stdout.write('\ndriver telah sampai                        \n')
    for i in range (20):
        sys.stdout.write('\rdriver mengantar ke lokasi tujuan |')
        time.sleep(0.1)
        sys.stdout.write('\rdriver mengantar ke lokasi tujuan /')
        time.sleep(0.1)
        sys.stdout.write('\rdriver mengantar ke lokasi tujuan -')
        time.sleep(0.1)
        sys.stdout.write('\rdriver mengantar ke lokasi tujuan \\')
        time.sleep(0.1)
    sys.stdout.write('\ndriver telah mengantar sampai di lokasi tujuan  \n')
    print('silahkan melakukan Pembayaran')

def login(slogin):
  print('login Ojek Online Syariah')
  while True:
    username = input('username : ')
    passw = input('password : ')
    
    if username == 'Luthfi' and passw == '082' or username == 'Adit' and passw == '110' or username == 'puput' and passw == '074': 
       slogin = 1
       return slogin 
       break
    elif username == 'amel' and passw == '123' or username == 'iin' and passw == '022' :
      slogin = 0
      return slogin
      break
    else:
       print('silahkan antum memasukkan password/username dengan benar!')
       continue

def menu(slogin):
  while True:
    print('---------------------------------')
    print('-------Ojek Online Syariah-------')
    print('--Membantu Antum dalam Berpergian--')
    print('------Aman,Nyaman,Terpercaya------')
    print('---------------------------------')
    print('Menu')
    print('1. OjekS')
    print('0. Keluar')
    inmenu = input('masukkan pilihan : ')
    if inmenu == '1' :
      break
    elif inmenu == '0' :
      print('Antum telah logout')
      print('Jazakallah khair telah menggunakan program kami')
      exit()
    else:
      continue
  
  while True:
    print('Kendaraan')
    print('1. Motor\n2. Mobil')
    kendaraan = input('masukan pilihan: ')
    if kendaraan == '1':
        harga_km = 500
        print('Antum memilih motor\n')
        break
    elif kendaraan == '2':
        harga_km = 750
        print('Antum memilih mobil\n')
        break
    else :
      continue

  while True:
    if (slogin == 1):
      print('Lokasi Penjemputan')
      list_jalanan(True)
      print('==============')
      print('1. Masukkan Lokasi Penjemputan')
      print('2. Menambahkan lokasi penjemputan')
      print('3. Mengupdate lokasi penjemputan')
      print('4. Menghapus lokasi penjemputan')
      print('5. Keluar Program')

      inputjemput = input('masukan pilihan: ')
      if inputjemput == '1':
        break
      elif inputjemput == '2':
        tambah(True)
      elif inputjemput == '3':
        update(True)
      elif inputjemput == '4':
        hapus(True)
      elif inputjemput == '5':
        exit()
      else:
        continue
    else: 
      print('Lokasi Penjemputan')
      list_jalanan(True)
      print('==============')
      break

  while True:
    jemput = input('Masukkan Lokasi Penjemputan: ')
    jemput = jemput.upper()
    if jemput in ojek['penjemputan']:
      break
    else:# No user prompt was found 
      print("Tidak ada lokasi")
      continue

  while True:
    if (slogin == 1):
      print('Lokasi Tujuan')
      list_jalanan(False)
      print('==============')
      print('1. Masukkan Lokasi Tujuan')
      print('2. Menambahkan lokasi Tujuan')
      print('3. Mengupdate lokasi Tujuan')
      print('4. Menghapus lokasi Tujuan')
      print('5. Keluar Program')
      inputtujuan = input('masukan pilihan: ')
      if inputtujuan == '1':
        break
      elif inputtujuan == '2':
        tambah(False)
      elif inputtujuan == '3':
        update(False)
      elif inputtujuan == '4':
        hapus(False)
      elif inputtujuan == '5':
        exit()
      else:
        continue
    else:
      print('Lokasi Tujuan')
      list_jalanan(False)
      print('==============')
      break

  while True:
    intujuan = input('Masukkan Lokasi Tujuan: ')
    intujuan = intujuan.upper()
    if intujuan in ojek['tujuan']:
    	jarak = (len(jemput)) * (len(intujuan))
    	break
    else:# No user prompt was found 
      print("Tidak ada lokasi")
      continue

  while True:
    print('Driver')
    print('1. Ikhwan\n2. Akhwat')
    driver = input('masukan pilihan: ')
    if driver == '1':
      urutan= jarak % len(ojek['ikhwan'])
      print('\nNama driver antum : '+str( ojek['ikhwan'][urutan]))
      break
    elif driver == '2':
      urutan= jarak % len(ojek['akhwat'])  
      print('\nNama driver antum : '+str( ojek['akhwat'][urutan]))
      break
    else:
      continue

  total = jarak * harga_km
  print("Titik Penjemputan : "+str(jemput))
  print("Titik Tujuan : "+str((intujuan)))
  print('Total Pembayaran '+str(total))
  menuju()

  while True:
   try:
   	Bayar=int(input("Jumlah Nominal Uang = Rp. ", ))
   except ValueError:
   	print ("Silahkan Antum Periksa lagi Inputan")
   	continue
   else :
   	if total <= Bayar:
   		Kembalian= (Bayar-total)
   		print("Uang Kembalian = ", "Rp.",Kembalian)
   		break
   	else:
   		print("Uang Anda Kurang")
   		continue


slogin = login(0)
while True:
 menu(slogin) 
 while True:
  pilihan=input('Apakah antum mau memesan ojek online syariah lagi ? y/t = ')
  if pilihan=='t':
    print('Terima kasih telah menggunakan program kami')
    exit()
  elif pilihan=='y':
    break
  else:
    continue