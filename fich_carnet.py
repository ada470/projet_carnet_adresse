class Personne:
    def __init__(self, p, n, tel, em):
        self.prenom = p
        self.nom = n
        self.numT = tel 
        self.em = em

    def __str__(self):
        return f"{self.prenom} {self.nom}\nemail: {self.em}\nNum de téléphone: {self.numT}"

class Travailleur(Personne):
    def __init__(self, p, n, tel, em, a, numE):
        Personne.__init__(self, p, n, tel, em)
        self.adresse = a
        self.numE = numE

    def __str__(self):
        return f"{Personne.__str__(self)}\nAdresse: {self.adresse}\nNum entreprise: {self.numE}"

class CarnetAdresses:
    def __init__(self):
        self.contacts = []

    def __str__(self):
        r = ""
        for i in self.contacts:
            r += f"{i}\n"
        return r

    def ajout_contact(self, P):
        self.contacts.append(P)

    def chercher_contact_nom_et_prenom(self, nr, pr=None):
        for per in self.contacts:
            if (nr == per.nom and pr is None) or (nr == per.nom and pr == per.prenom):
                print(per)

    def chercher_contact_nom(self, nr):
        for per in self.contacts:
            if nr == per.nom:
                print(per)

    def menu(self):
        print("1. Ajout d'une personne")
        print("2. Ajout d'un travailleur")
        print("3. Recherche d'un contact")
        print("4. Affichage du carnet")
        print("0. Quitter")
        choix = input("Entrer votre choix : ")
        return choix

C = CarnetAdresses()
while True:
    choix = C.menu()
    if choix == "1":
        p = input("Entrer le prénom de la personne : ")
        n = input("Entrer son nom : ")
        while True:
            em = input("Entrer son email : ")
            if "@" in em:
                break
            else:
                print("Email invalide, veuillez réessayer.")
        while True:
            try:
                tel = int(input("Entrer son numéro de téléphone : "))
                break
            except ValueError:
                print("Saisie incorrecte, veuillez réessayer.")
        P = Personne(p, n, tel, em)
        C.ajout_contact(P)
    elif choix == "2":
        p = input("Entrer le prénom du travailleur : ")
        n = input("Entrer le nom du travailleur : ")
        while True:
            try:
                tel = int(input("Entrer le numéro du travailleur : "))
                break
            except ValueError:
                print("Saisie incorrecte, veuillez réessayer.")
        while True:
            em = input("Entrer son email : ")
            if "@" in em:
                break
            else:
                print("Email invalide, veuillez réessayer.")
        a = input("Entrer l'adresse de l'entreprise : ")
        while True:
            try:
                numE = input("Entrer le numéro de l'entreprise : ")
                assert numE>0
                break
            except AssertionError:
                print("saisie incorrecte,ressayer")
            except ValueError:
                print("saisie incorrecte,ressayer")
        T = Travailleur(p, n, tel, em, a, numE)
        C.ajout_contact(T)
    elif choix == "3":
        print("1. Recherche par nom ")
        print("2. Recherche par nom et prénom  ")
        print("0. Quitter ")
        choix2 = input("Entrer votre choix : ")
        if choix2 == "1":
            nr = input("Entrer le nom à rechercher : ")
            C.chercher_contact_nom(nr)
            print("1. Recherche par nom ")
            print("2. Recherche par nom et prénom  ")
            print("0. Quitter ")
            choix2 = input("Entrer votre choix : ")
        elif choix2 == "2":
            nr = input("Entrer le nom à rechercher : ")
            pr = input("Entrer son prénom : ")
            C.chercher_contact_nom_et_prenom(nr, pr)
            print("1. Recherche par nom ")
            print("2. Recherche par nom et prénom  ")
            print("0. Quitter ")
            choix2 = input("Entrer votre choix : ")
        elif choix2 == "0":
            continue
    elif choix == "4":
        print(C)
    elif choix == "0":
        break
    else:
        print("Choix invalide, veuillez réessayer.") 