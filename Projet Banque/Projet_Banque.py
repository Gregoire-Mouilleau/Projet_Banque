 class CompteBancaire:
    def __init__(self, idNumber, nomPrenom, solde):
        self.idNumber = idNumber
        self.nomPrenom = nomPrenom
        self.solde = solde
        
    def versement(self, argent):
        self.solde = self.solde + argent
    
    def retrait(self, argent):
        if self.solde < argent:
            print("Impossible d'effectuer l'operation. Solde insuffisant !")
        else:
            self.solde = self.solde - argent
    
    def __str__ (self):
        return 