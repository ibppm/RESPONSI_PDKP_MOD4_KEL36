class method:
    key = int(input('\n\nMasukkan jumlah perubahan yang anda inginkan : '))

    def decode(kalimat,cipher_key):
      abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
      kalimat = kalimat.lower()
      hasil_decode = ''
      for karakter in kalimat:
        if karakter in abjad:
          daftar_lama = abjad.index(karakter)
          daftar_baru = (daftar_lama - cipher_key ) % len(abjad)
          abjad_baru = abjad[daftar_baru]
          hasil_decode = hasil_decode + abjad_baru 
        else:
           hasil_decode = hasil_decode + ' ' 
      return hasil_decode

    kalimat = input('\n\nMasukkan kalimat yang ingin didekripsi : ')

    # DEKRIPSI
    kalimat_hasil = decode(kalimat,key)
    print('\nHasil Dekripsi adalah : ', kalimat_hasil)