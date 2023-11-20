nom = "baguette"
prix = 2
stock = 10
print("nom:", nom)
print("prix:", prix)
print("stock:", stock)
quantite_achat = int(input("Veuillez mettre la quantité a acheter : "))
stock -= quantite_achat
prix += 0.2
print("\nAprès l'achat et l'ajustement du prix :")
print("nom:", nom)
print("prix (après inflation):", prix)
print("stock:", stock)