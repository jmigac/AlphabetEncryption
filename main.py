from matplotlib.pyplot import figure, imshow, axis
from matplotlib.image import imread


class Slovo():
    def __init__(self, naziv,link):
        super(Slovo, self).__init__()
        self.string = naziv
        self.putanja= link


def prikazSlikaHorizontalno(slovaFraze):
    fig = figure()
    number_of_files = len(slovaFraze)
    for i in range(number_of_files):
        a=fig.add_subplot(1,number_of_files,i+1)
        image = imread(slovaFraze[i].putanja)
        imshow(image,cmap='Greys_r')
        axis('off')
    fig.show()


if __name__ == "__main__":
    frazaZaKriptiranje = str(input("Unesite frazu za kriptiranje:"))
    upitZaKriptiranje = frazaZaKriptiranje.upper()
    rjecnikKriptiranja = {}
    nizSlova = []
    for slovo in upitZaKriptiranje:
        if(slovo != " "):
            novoSlovo = Slovo(slovo,'./alphabet/'+slovo+".jpg")
            nizSlova.append(novoSlovo)

prikazSlikaHorizontalno(nizSlova)
