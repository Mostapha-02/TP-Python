
# Demander à l'utilisateur de saisir le login et le mot de passe
login_saisi = input("Entrez votre login : ")
mot_de_passe_saisi = input("Entrez votre mot de passe : ")

# Vérifier si le login et le mot de passe sont corrects
if login_saisi == "admin" and mot_de_passe_saisi == "admin":
    print("Bienvenue ! Vous êtes connecté.")
else:
    print("Login ou mot de passe incorrect. Veuillez réessayer.")
