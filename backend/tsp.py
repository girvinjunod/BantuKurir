def edistance(k1, k2):
    x1 = k1[0]
    y1 = k1[1]
    x2 = k2[0]
    y2 = k2[1]
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def getDistance(arrayKoordinat):
    n = len(arrayKoordinat)
    jaraklokasi = [[0 for j in range(n)] for i in range(n)]
    #Isi jarak antar kota
    for i in range(n):
        for j in range(n):
            jaraklokasi[i][j] = edistance(arrayKoordinat[i], arrayKoordinat[j])
    return jaraklokasi

def tsp(awal, node, dist):
    #node mulai dri 0
    #Basis
    if node is None or len(node) == 0:
        return dist[awal][0], [awal]
    #Rekursi
    ans = []
    for i in range(len(node)):
        c = dist[awal][node[i]]
        sisa = node[:]
        rek = node[i]
        sisa.pop(i)
        f, lastnode = tsp(rek, sisa, dist)
        plus = c + f
        lastnode.append(awal)
        ans.append([plus, lastnode])
    mindist = ans[0][0]
    minroute = ans[0]
    for i in ans:
        if (i[0] < mindist):
            mindist = i[0]
            minroute = i
    res = minroute
    return res

    

def solveTSP(dist, awal):
    n = len(dist)
    if n == 1:
        return 0
    if n == 2:
        return 2*(dist[0][1])
    node = []
    for i in range(1, n):
        node.append(i)
    res, jalur = tsp(awal,node,dist)
    jalur.reverse()
    jalur.append(awal)
    return res, jalur

def getJalurNama(jalur,namalokasi):
    nama = ""
    listnama = []
    for i in range(len(jalur)):
        nama += namalokasi[jalur[i]]
        listnama.append(namalokasi[jalur[i]])
        if i != len(jalur)-1:
            nama += "-"
    return nama, listnama

def out(res,jalur,namalokasi):
    string= []
    string.append("Jalur terpendek: " + getJalurNama(jalur,namalokasi)[0])
    string.append("Jarak: " + str(res))
    return string, getJalurNama(jalur,namalokasi)[1]


def intermediates(p1, p2, nb_points=8):
    """"Return a list of nb_points equally spaced points
    between p1 and p2"""
    # If we have 8 intermediate points, we have 8+1=9 spaces
    # between p1 and p2
    x_spacing = (p2[0] - p1[0]) / (nb_points + 1)
    y_spacing = (p2[1] - p1[1]) / (nb_points + 1)

    return [[p1[0] + i * x_spacing, p1[1] +  i * y_spacing] 
            for i in range(1, nb_points+1)]

if __name__ == '__main__':
    #input
    namalokasi = ["Perusahaan", "Indomaret", "Neraka", "ITB", "Rumah Yahya"]
    koorlokasi = [[0,0], [3,4], [12,3], [-5,-7], [6,-3]]

    #Isi jarak antar kota
    jaraklokasi = getDistance(koorlokasi)


    tes= [
        [0,10,15,20],
        [5,0,9,10],
        [6,13,0,12],
        [8,8,9,0]]
    #Solve TSP
    res, jalur = solveTSP(jaraklokasi, 0)
    print(out(res,jalur,namalokasi))
