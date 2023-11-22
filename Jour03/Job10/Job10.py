def pair_ou_impair(nombre):
    if type(nombre) == int and nombre > 0:
        if nombre % 2 == 0:
            print("Le chiffe est pair")
        else:
            print("Le chiffre est impair")
    else:
        print("Le chiffre doit être un entier positif")
        
pair_ou_impair(9)
pair_ou_impair(-7)
pair_ou_impair(-78)
pair_ou_impair(128)