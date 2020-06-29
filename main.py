# Parseaa kotuksen sanalistan piirtopeliä skribbl.io varten

# otetaan sanoista vain joka N:s
N = 10
# anna arvo väliltä [0, N-1], määrittää mukaanotettavat sanat
OFFSET = 0
# sallitut merkit
aakkoset = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö", "-"]
# sallittu minimipituus sanalle
MINPITUUS = 2
# sallittu maksimipituus sanalle
MAXPITUUS = 30

def lue_tiedosto():
    """
    lukee sanalistan "kotus-sanalista_v1.xml"
    :return sanat: list, halutut sanat listana
    """
    sanat = []

    with open("kotus-sanalista_v1.xml") as fp:
        for rivi in fp:
            if rivi.startswith("<st><s>"):
                alkuindex = len("<st><s>")
                loppuindex = rivi.index("</s>")

                # tarkista, että sanan pituus sallituissa rajoissa
                if loppuindex > alkuindex + MINPITUUS and loppuindex < alkuindex + MAXPITUUS:
                    tarkistin = True
                    sana = rivi.strip()[alkuindex:loppuindex]

                    for chara in sana:
                        merkkitarkistin = False
                        # Tarkistetaan ettei sisällä huonoja merkkejä (esim. é, â)
                        for aakkonen in aakkoset:
                            if aakkonen == chara or aakkonen.lower() == chara:
                                merkkitarkistin = True
                        if not merkkitarkistin:
                            tarkistin = False

                    # lisätään sana listaan, jos pituus OK ja sisältää vain sallittuja merkkejä
                    if  tarkistin:
                        sanat.append(sana)
    return sanat

def kirjoita_tiedosto(sanat):
    """
    kirjoittaa tiedoston, jossa sanat erotettu pilkulla, kirjoittaa vain joka N:nen sanan alkaen OFFSETistä
    :param sanat: list, tiedostosta saadut sanat
    :return:
    """

    i = 1
    with open("sanat.txt", "w") as fp:
        for rivi in sanat:
            if i % N-1 == OFFSET:
                fp.write("{}, ".format(rivi))
            i += 1


def main():
    sanat = lue_tiedosto()
    kirjoita_tiedosto(sanat)

main()