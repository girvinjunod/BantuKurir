def parsing(file):
    a = file.split("\n")
    if (len(a) != 5):
        return "Salah format"
    namalokasi = a[0]
    koordinatlokasi = a[1]
    identitas = a[2]
    waktu = a[3]
    kecepatan = a[4]
    if ("Nama Lokasi:" not in a[0]):
        return "Salah format"
    if ("Koordinat:" not in a[1]):
        return "Sala format"
    if ("Identitas Kurir:" not in a[2]):
        return "Salah format"
    if ("Waktu Pengiriman:" not in a[3]):
        return "Salah format"
    if ("Kecepatan Rata-rata Kurir:" not in a[4]):
        return "Salah format"
    try:
        namalokasi = namalokasi[namalokasi.index(":")+1:].replace(" ","")
        namalokasi = namalokasi.split(",")
    except:
        return "Salah format"
    try:
        koordinatlokasi = koordinatlokasi[koordinatlokasi.index(":")+1:].replace(" ","")
        koordinatlokasi = koordinatlokasi.replace("(","").replace(")","").split("|")
        for i in range(len(koordinatlokasi)):
            temp = koordinatlokasi[i]
            temp = temp.split(",")
            temp[0] = float(temp[0])
            temp[1] = float(temp[1])
            koordinatlokasi[i] = temp
    except:
        return "Salah format"

    if (len(namalokasi) != len(koordinatlokasi)):
        return "Salah format"

    try:
        identitas = identitas[identitas.index(":")+1:].strip()
    except:
        return "Salah format"
    try:
        waktu = waktu[waktu.index(":")+1:].strip().split(":")
        waktu = [int(i) for i in waktu]
        if (waktu[0] < 0 or waktu[0] > 23 or waktu[1] < 0 or waktu[1] > 59 or waktu[2] < 0 or waktu[2] > 59):
            return "Salah format"
        waktu = str(waktu[0]) + ":" + str(waktu[1]) + ":" + str(waktu[2])
    except:
        return "Salah format"
    try:
        kecepatan = kecepatan[kecepatan.index(":")+1:].strip()
        kecepatan = float(kecepatan)
    except:
        return "Salah format"

    return namalokasi, koordinatlokasi, identitas, waktu, kecepatan

def parseMultiple(arrayFile):
    try:
        anamalokasi = []
        akoorlokasi = []
        aidentitas = []
        awaktu = []
        akecepatan = []
        for i in arrayFile:
            namalokasi, koordinatlokasi, identitas, waktu, kecepatan = parsing(i)
            anamalokasi.append(namalokasi)
            akoorlokasi.append(koordinatlokasi)
            aidentitas.append(identitas)
            awaktu.append(waktu)
            akecepatan.append(kecepatan)
        return [True,anamalokasi,akoorlokasi,aidentitas,awaktu,akecepatan]
    except:
        return [False]



if __name__ == '__main__':
    tes ='''Nama Lokasi: Perusahaan, ITB
    Koordinat: (0,0) | (1.5, 6.9)
    Identitas Kurir: Joko
    Waktu Pengiriman: 12:12:12
    Kecepatan Rata-rata Kurir: 4.20'''
    tes1='''Nama Lokasi: Perusahaan, McD
    Koordinat: (0,0) | (1.5, 4.20)
    Identitas Kurir: Jokowi
    Waktu Pengiriman: 12:12:12
    Kecepatan Rata-rata Kurir: 6.9'''
    print(parseMultiple([tes,tes1]))
