class batiment : 
    def __init__(self,ad):
        self.ad = ad 
    def getad(self) :
        return self.ad
    def setad (self , add) :
        self.ad = add
    def __str__(self):
        return 'laderresse de batmient est : {}'.format(self.ad)
           
class maison(batiment) : 
    def __init__(self, ad , nbp):
        super().__init__(ad)
        self.nbp =nbp
    def getnbp (self) :
        return self.nbp
    def setnbp (self,no) : 
            self.nbp = no
    def __str__(self) :
        return'maison (laddresse({}) , et le nombre de piece {}'.format(self.ad , self.nbp)

class  Immeuble(batiment) :
    def __init__(self, ad, nbapp):
        super().__init__(ad)    
        self.nbapp = nbapp
    def getnbapp(self):
        return self.nbapp
    def setnbapp(self,nb):
        self.nbapp = nb
    def __str__(self):
        return'immeuble (ladresee {} et le nombre des appartement {})'.format(self.ad , self.nbapp)

imb =   Immeuble("hay mly rissani" , 23)
print(imb)
                 
