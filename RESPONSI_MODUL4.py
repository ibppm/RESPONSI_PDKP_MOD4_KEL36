print("===== SELAMAT DATANG DI PROGRAM ENKRIPSI DAN DEKRIPSI KELOMPOK 36 =====")
print("\n\nSilahkan pilih MODE yang ingin anda gunakan : 1. ENKRIPSI")
print("                                              2. DEKRIPSI")   

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

mode = int(input("\nSilahkan masukan nomor pilihan MODE yang anda inginkan : "))

if mode==1:
    key = int(input('\n\nMasukkan jumlah perubahan yang anda inginkan : '))

    def encode(kalimat,cipher_key):
      kalimat = kalimat.lower()
      hasil_encode = ''
      for karakter in kalimat:
        if karakter in abjad:
          daftar_lama = abjad.index(karakter)
          daftar_baru = (daftar_lama + cipher_key ) % len(abjad)
          abjad_baru = abjad[daftar_baru]
          hasil_encode = hasil_encode + abjad_baru 
        else:
           hasil_encode = hasil_encode + ' ' 
      return hasil_encode

    kalimat = input('\n\nMasukkan kalimat yang ingin dienkripsi : ')

    # ENKRIPSI
    kalimat_hasil = encode(kalimat,key)
    print("\nHasil Enkripsi adalah : ", kalimat_hasil)



elif mode==2:
    import DEKRIPSI
    get_class = DEKRIPSI.method()
