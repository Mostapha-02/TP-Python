from abc import ABC, abstractmethod

class Employe(ABC):
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def getnm(self):
        return self.nom

    def getprnm(self):
        return self.prenom

    def setnm(self, nm):
        self.nom = nm

    def setprnm(self, prnm):
        self.prenom = prnm

    def __str__(self):
        return "person(nom: {}, prenom: {})".format(self.nom, self.prenom)

    @abstractmethod
    def gains(self):
        pass  # Cette méthode doit être implémentée dans les sous-classes


class Patron(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom)
        self.salaire = salaire

    def getsal(self):
        return self.salaire

    def setsal(self, sl):
        self.salaire = sl

    def __str__(self):
        return "personne({} , salaire: {})".format(super().__str__(), self.salaire)

    def gains(self):
        return self.salaire


class TravailleurCommission(Employe):
    def __init__(self, nom, prenom, salaire, commission, quantite):
        super().__init__(nom, prenom)
        self.salaire = salaire
        self.commission = commission
        self.quantite = quantite

    def getsl(self):
        return self.salaire

    def getcom(self):
        return self.commission

    def getq(self):
        return self.quantite

    def setsl(self, sl):
        self.salaire = sl

    def setcom(self, com):
        self.commission = com

    def setq(self, q):
        self.quantite = q

    def __str__(self):
        return "personne({}, salaire: {}, commission: {}, quantite: {})".format(
            super().__str__(), self.salaire, self.commission, self.quantite
        )

    def gains(self):
        return self.salaire + (self.commission * self.quantite)


class TravailleurHoraire(Employe):
    def __init__(self, nom, prenom, retribution, heures):
        super().__init__(nom, prenom)
        self.retribution = retribution
        self.heures = heures

    def getre(self):
        return self.retribution

    def geth(self):
        return self.heures

    def setre(self, re):
        self.retribution = re

    def seth(self, h):
        self.heures = h

    def __str__(self):
        return "personne({}, retribution: {}, heures: {})".format(
            super().__str__(), self.retribution, self.heures
        )

    def gains(self):
        return self.retribution * self.heures


# Exemple d'utilisation
patron = Patron("Dupont", "Jean", 5000)
travailleur_commission = TravailleurCommission("Martin", "Sophie", 2000, 0.1, 100)
travailleur_horaire = TravailleurHoraire("Lefevre", "Pierre", 15, 120)

employes = [patron, travailleur_commission, travailleur_horaire]

for employe in employes:
    print(employe)
    print(f"Salaire/Gains: {employe.gains()}")
    print("-" * 30)


