meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print('Artinya: ')
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak
    print('Maaf kata belum tersedia/belum di update')
