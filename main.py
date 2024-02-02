#subor_na_citanie = open("habibi.txt","r",encoding="UTF-8")

#niekolko sposobov ako pracovat s obsahom suboru
#cislo 1

#for riadok in subor_na_citanie:
 #print(riadok) #riadok = string
#pri tomto spracovani su dva entery lebo jeden je zo suboru a druhy z printu
    #print(riadok.strip()) #odstranime entery

# cislo 2
#riadok = subor_na_citanie.readline() #readline = citacia hlava, precita len jeden riadok
#print(riadok)
#print("---------")
#for riadok in subor_na_citanie:
    #print(riadok.strip()) # tento cyklus uz vypisal len riadky zvysne
# tento postup budeme vyuzivat pri suboroch, kde prvy riadok potrebujes spracovat inak ako ostatne

#cislo 3
#riadky = subor_na_citanie.readlines()
#print(riadky) #vypise zoznam
 # + znak enteru \n
 # cesty k zoznamu ktore mozeme zadat su RELATIVNE alebo ABSOLUTNY
 # ak davam backslash musim dat dva \\
 # absolutna
 # subor_na_citanie=open("D:\\test\\jozo.txt","r", encoding="UFT-8")
 # subor_na_citanie=open("D:/test/jozo.txt","r", encoding="UFT-8")
 # relativna
 #len v urcitom adresari, ked potrebujem vyjst z absolutneho adresara
 #subor_na_citanie=("../gol/troj.py az po koniec)
 #dat do toho isteho adresara s ktorym pracuje

#fr = open("hada.txt","r", encoding="UFT-8")
#fw = open("vystup.txt","w", encoding="UTF-8") #ak ten subor neexistuje vytvori ho

def spracuj(riadok):
    #tu nieco vymyslis
    counter = 1
    for i in range(0,len(riadok)-1):
        #print(i,r[i])
        if riadok[i]==riadok[i+1]:
            counter += 1
            if i == len(riadok)-2:
                print(riadok[i] + str(counter), end="")
        else:
            print(riadok[i]+str(counter), end="")
            counter = 1
            if i == len(riadok)-2:
                print(riadok[i+1] + "1", end="")

spracuj("HHHHDDDLLPPH")
    #return
#for row in fr:
    #vysledok = spracuj(row.strip()) #tu bude to h4...
    #fw.write(vysledok)

#fw.close()  #zatvori subor na zapisovanie



def checkio(zoznam:list):
    pom_zoz = [] #tu budem uchovavat pocetnost jednotlivych znakov
    finalzoz = [] #naplnim tymi co su tam viac ako raz
    for i in zoznam: # v tomto fore pocitam pocetnost jednotlivych znakov
        pom_zoz.append(zoznam.count(i))
    #print(zoznam,pom_zoz)
    for i in range(len(zoznam)): #ak je pocetnost znaku viac ako jedna, vlozim znak do noveho zoznamu
        if pom_zoz [i]>1:
            finalzoz.append(zoznam[i])
    return finalzoz

assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
assert list(checkio([1, 2, 3, 4, 5])) == []
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
assert list(checkio([10, 20, 30, 10])) == [10, 10]
assert list(checkio([7])) == []
assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
assert list(checkio([99, 98, 99])) == [99, 99]
assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]

zoznam2 = ["a", "b", "c", "a", "b", "a"]
def most_frequent(zoznam):
    pocet = 0
    najcastejsie = ""
    for i in zoznam2:
        if zoznam2.count(i) > pocet:
            pocet = zoznam2.count(i)
            najcastejsie = i
    return najcastejsie
print(most_frequent(zoznam2))
j

