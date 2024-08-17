# Nom: Lama Youssef
# Date: 6 Novembre, 2022
# nom du programme: Restaurant
# But: D'etre capable d'avoir un menu qui va avoir l'option de choisir la quantité et
# d'afficher plusieurs prix en utilisant des boutons et frames

import tkinter
from tkinter import *
from PIL import Image, ImageTk

# Numéros de départ des différents éléments
nom_element_selectionne = ""
prix_element_selectionne = 0
elements_totale = 0
quantite_selectionne = 1
sous_prix_totale = 0


# Crée la fenêtre
win = Tk()
win.title("Restaurant simulator")
win.geometry("1324x894")
win.configure(bg="#64605A")
win.minsize(width=1320, height=910)
win.maxsize(width=1320, height=910)


# ---------------------------------Crée les 2 Frames pour la section de banniere et la resto---------------------------------
frame_banniere = LabelFrame(win, bg="#EFEAE9", width=1305, height=250)
frame_banniere.grid(row=0, column=0, sticky="N")

frame_principale = Frame(win, bg="#EFEAE9", width=1305, height=640)
frame_principale.grid(row=1, column=0, sticky="S", padx=3, pady=3)



# ---------------------------------3 frames principales pour chaques section de la restaurant---------------------------------
menu_frame = LabelFrame(frame_principale, text="Affiche ce que tu veux commander", fg="white", bg="#64605A", width=400, height=28)
menu_frame.grid(row=0, column=0, padx=3, pady=3, sticky="W")

frame_affichage = LabelFrame(frame_principale, text="NB : Si vous ne voulez pas quelque chose, assurez-vous d'appuyer\nsur retirer avant d'afficher un autre aliment", labelanchor="n", fg="white", bg="#64605A", width=482, height=28)
frame_affichage.grid(row=0, column=1, padx=3, pady=3)

frame_facture = LabelFrame(frame_principale, text="Appuyez sur commander pour profiter de votre repas!", labelanchor="n", fg="white", bg="#7F7774", width=400, height=28)
frame_facture.grid(row=0, column=2, padx=3, pady=3, sticky="E")


# --------------------------------------------------------liste de menu--------------------------------------------------------
frame_etiquette_menu = Frame(menu_frame, bg="#C68E8E", width=400, height=50)
frame_etiquette_menu.grid(row=0, column=0, padx=3, pady=3, sticky="N")
menu_etiquette = Label(frame_etiquette_menu, text="Menu~", font=("Helvetica", 14, "bold"), anchor="center", bg="#C68E8E", fg="white", width=32, height=3)
menu_etiquette.grid(row=0, column=0, sticky="N")

frame_eau = Frame(menu_frame, bg="#EBD4CF", width=40, height=5)
frame_eau.grid(row=1, column=0, pady=3)
etiquette_eau = Label(frame_eau, text="L'eau...1,20$", font=("Comic Sans MS", 14), anchor="center", bg="#C68E8E", fg="white", width=24, height=3)
etiquette_eau.grid(row=0, column=0, )

frame_shawarma = Frame(menu_frame, bg="#EBD4CF", width=40, height=5)
frame_shawarma.grid(row=2, column=0, pady=3)
etiquette_shawarma = Label(frame_shawarma, text="Shawarma...13,99$", font=("Comic Sans MS", 14), anchor="center", bg="#C68E8E", fg="white", width=24, height=3)
etiquette_shawarma.grid(row=0, column=0)

frame_kofta = Frame(menu_frame, bg="#EBD4CF", width=40, height=5)
frame_kofta.grid(row=3, column=0, pady=3)
etiquette_kofta = Label(frame_kofta, text="Kofta...9,45$", font=("Comic Sans MS", 14), anchor="center", bg="#C68E8E", fg="white", width=24, height=3)
etiquette_kofta.grid(row=0, column=0)

frame_dolma = Frame(menu_frame, bg="#EBD4CF", width=40, height=5)
frame_dolma.grid(row=4, column=0, pady=3)
etiquette_dolma = Label(frame_dolma, text="Dolma...7,99$", font=("Comic Sans MS", 14), anchor="center", bg="#C68E8E", fg="white", width=24, height=3)
etiquette_dolma.grid(row=0, column=0)

frame_baklava = Frame(menu_frame, bg="#EBD4CF", width=40, height=5)
frame_baklava.grid(row=5, column=0, pady=3)
etiquette_baklava = Label(frame_baklava, text="Baklava...11,99$", font=("Comic Sans MS", 14), anchor="center", bg="#C68E8E", fg="white", width=24, height=3)
etiquette_baklava.grid(row=0, column=0)

frame_knafeh = Frame(menu_frame, bg="#EBD4CF", width=40, height=5)
frame_knafeh.grid(row=6, column=0, pady=3)
etiquette_knafeh = Label(frame_knafeh, text="Knafeh...5,99$", font=("Comic Sans MS", 14), anchor="center", bg="#C68E8E", fg="white", width=24, height=3)
etiquette_knafeh.grid(row=0, column=0)

# ----------------------------------------------Section variable pour ajouter des photos--------------------------------------
def select_menu_image(nom_element, prix_element, chemin_image):
    global attendre
    global affichage_etiquette
    global nom_element_selectionne
    global prix_element_selectionne
    image_objet = Image.open(chemin_image).resize((500, 525))
    imagess = ImageTk.PhotoImage(image_objet, width=500, height=365)
    attendre.configure(image=imagess)
    attendre.image = imagess
    affichage_etiquette["text"] = nom_element
    nom_element_selectionne = nom_element
    prix_element_selectionne = prix_element
    ajoute_btn["state"] = NORMAL

# --------------------------------------------Section pour choisir la quantité------------------------------------------------
def choisir_une_quantite(q=1):
    global quantite_selectionne
    quantite_selectionne = q

# ------------------------------------Section pour acheter les assiettes et créer la total-------------------------------------
def achete_assiette():
    global nom_element_selectionne
    global prix_element_selectionne
    global elements_totale
    global frame_facture
    global quantite_selectionne
    global facture_totale_titre
    global sous_prix_totale
    global facture_label


    if nom_element_selectionne:
        facture_label = Label(facture_section_frame, text=str(quantite_selectionne) + " " + nom_element_selectionne + " Sous-totale: " + str(prix_element_selectionne * quantite_selectionne), bg="#64605A", fg="white")
        facture_label.grid(row=elements_totale, column=0, sticky="nw")
        ajoute_btn["state"] = DISABLED
        elements_totale += 1
        sous_prix_totale += prix_element_selectionne * quantite_selectionne
        prix_totale = (sous_prix_totale * 0.13) + sous_prix_totale
        facture_totale_titre["text"] = "SOUS-PRIX : " + "{:.2f}".format(sous_prix_totale) + "$     "\
                                                                                               "\nTOTALE :   " + "{:.2f}".format(prix_totale) + "$"

# -------------------------------------Section pour supprimer les assiettes et la total--------------------------------------
def supprime_assiette():
    global nom_element_selectionne
    global prix_element_selectionne
    global elements_totale
    global frame_facture
    global quantite_selectionne
    global facture_totale_titre
    global sous_prix_totale
    global facture_label

    if nom_element_selectionne:
        facture_label.destroy()
        ajoute_btn["state"] = NORMAL
        elements_totale -= 1
        sous_prix_totale -= prix_element_selectionne * quantite_selectionne
        prix_totale = (sous_prix_totale * 0.13) + sous_prix_totale
        if prix_totale <= 0:
            facture_totale_titre["text"] = "SOUS-PRIX :   00,00$"\
                                           "\nTOTALE :   00,00$"
        else:
            facture_totale_titre["text"] = "SOUS-PRIX :   " + "{:.2f}".format(sous_prix_totale) + "$     "\
                                                                                              "\nTOTALE :   " + "{:.2f}".format(prix_totale) + "$"

# -------------------------------------Section pour souhaiter un bon repas à l'utilisateur--------------------------------------
def changer_a_au_revoir():
    au_revoir_frame = Frame(win, bg="green", width=1320, height=894,)
    au_revoir_frame.grid()
    frame_principale.destroy()
    frame_banniere.destroy()
    au_revoir_titre = Label(au_revoir_frame, text="Au revoir! Merci de venir! Bon appétit!", anchor= "center",font=("Comic Sans MS", 25), bg="#64605A", fg="#D1D1D1")
    au_revoir_titre.grid(row=0, column=0)



# -------------------------------------Section pour les bouttons pour afficher les assiettes--------------------------------------
eau_affichage = tkinter.Button(frame_eau, font=("Comic Sans MS", 10), text="Affiche", bg="#C68E8E", fg="white", command=lambda:  select_menu_image("L'eau", 1.20, "Eau_Nourriture_Stable.jpg"))
eau_affichage.grid(row=0, column=2, sticky="E", padx=25)

shawarma_affichage = tkinter.Button(frame_shawarma, font=("Comic Sans MS", 10), text="Affiche", bg="#C68E8E", fg="white", command=lambda:  select_menu_image("Shawarma", 13.99, "Shawarma_Nourriture_Stable.jpg"))
shawarma_affichage.grid(row=0, column=2, sticky="E",  padx=25)

kofta_affichage = tkinter.Button(frame_kofta, font=("Comic Sans MS", 10), text="Affiche", bg="#C68E8E", fg="white", command=lambda:  select_menu_image("Kofta", 9.45, "Kofta_Nourriture_Stable.jpg"))
kofta_affichage.grid(row=0, column=2, sticky="E",  padx=25)

dolma_affichage = tkinter.Button(frame_dolma, font=("Comic Sans MS", 10), text="Affiche", bg="#C68E8E", fg="white", command=lambda:  select_menu_image("Dolma", 7.99, "Dolma_Nourriture_Stable.jpg"))
dolma_affichage.grid(row=0, column=2, sticky="E",  padx=25)

baklava_affichage = tkinter.Button(frame_baklava, font=("Comic Sans MS", 10), text="Affiche", bg="#C68E8E", fg="white", command=lambda:  select_menu_image("Baklava", 11.99, "Baklava_Nourriture_Stable.jpg"))
baklava_affichage.grid(row=0, column=2, sticky="E",  padx=25)

knafeh_affichage = tkinter.Button(frame_knafeh, font=("Comic Sans MS", 10), text="Affiche", bg="#C68E8E", fg="white", command=lambda:  select_menu_image("Knafeh", 5.99, "Knafeh_Nourriture_Stable.jpg"))
knafeh_affichage.grid(row=0, column=2, sticky="E",  padx=25)


# -------------------------------------Tous ce qui est dans la cadre_affichage--------------------------------------
frame_affichage_etiquette = Frame(frame_affichage, bg="#C68181", width=40, height=28)
frame_affichage_etiquette.grid(row=0, column=0, sticky="N", padx=3, pady=3)
affichage_etiquette = Label(frame_affichage_etiquette, text="Affiche", font=("Helvetica", 14, "bold"), anchor="center", bg="#C68181", fg="white", width=42, height=2)
affichage_etiquette.grid(row=0, column=0, sticky="N")

attendre_image_frame = Frame(frame_affichage, bg="#C68181", width=500, height=300)
attendre_image_frame.grid(row=1, column=0, padx=3, pady=3)

quantite_btns_frame = LabelFrame(frame_affichage, text="Choisir une quantité", fg="white", bg="#C68181", width=500, height=58)
quantite_btns_frame.grid(row=2, column=0, padx=3, pady=3)

btns_frame = Frame(frame_affichage, bg="#C68181", width=500, height=58)
btns_frame.grid(row=3, column=0, padx=3, pady=3)

assiette_btn_1 = tkinter.Radiobutton(quantite_btns_frame, indicatoron=False, value="click", text="1 assiette", font=("Comic Sans MS", 9), bg="#C68E8E", fg="#DABDC5", anchor="center", width=20, height=2, command=lambda: choisir_une_quantite(1))
assiette_btn_1.grid(row=0, column=0, padx=2, pady=2)
assiette_btn_2 = tkinter.Radiobutton(quantite_btns_frame, indicatoron=False, value="click1", text="2 assiettes", font=("Comic Sans MS", 9), bg="#C68E8E", fg="#DABDC5", anchor="center", width=20, height=2, command=lambda: choisir_une_quantite(2))
assiette_btn_2.grid(row=0, column=1, padx=2, pady=2)
assiette_btn_3 = tkinter.Radiobutton(quantite_btns_frame, indicatoron=False, value="click2", text="3 assiettes", font=("Comic Sans MS", 9), bg="#C68E8E", fg="#DABDC5", anchor="center", width=20, height=2, command=lambda: choisir_une_quantite(3))
assiette_btn_3.grid(row=0, column=2, padx=2, pady=2)
assiette_btn_4 = tkinter.Radiobutton(quantite_btns_frame, indicatoron=False, value="click3", text="4 assiettes", font=("Comic Sans MS", 9), bg="#C68E8E", fg="#DABDC5", anchor="center", width=31, height=2, command=lambda: choisir_une_quantite(4))
assiette_btn_4.grid(row=1, column=0, sticky="W",columnspan=2, padx=2, pady=2)
assiette_btn_5 = tkinter.Radiobutton(quantite_btns_frame, indicatoron=False, value="click4", text="5 assiettes", font=("Comic Sans MS", 9), bg="#C68E8E", fg="#DABDC5", anchor="center", width=31, height=2, command=lambda: choisir_une_quantite(5))
assiette_btn_5.grid(row=1, column=1, sticky="E", columnspan=2, padx=2, pady=2)

ajoute_btn = tkinter.Button(btns_frame, text="Ajoute à la commande", font=("Comic Sans MS", 10), bg="#C68E8E", fg="white", anchor="center", width=32, height=2, command=achete_assiette)
ajoute_btn.grid(row=0, column=0, sticky="W", padx=2, pady=2)

retirer_btn = tkinter.Button(btns_frame, text="Retirer", font=("Comic Sans MS", 9), bg="#C68E8E", fg="white", anchor="center", width=32, height=2, command=supprime_assiette)
retirer_btn.grid(row=0, column=1, sticky="E", padx=2, pady=2)


# --------------------------------------Tous ce qui est dans la cadre_facture-----------------------------------------
frame_facture_etiquette = Frame(frame_facture, bg="#C68E8E", width=400, height=50)
frame_facture_etiquette.grid(row=0, column=0, sticky="N", padx=3, pady=3)
facture_titre = Label(frame_facture_etiquette, text="Facture", font=("Helvetica", 14, "bold"), anchor="center", bg="#C68E8E", fg="white", width=30, height=3)
facture_titre.grid(row=0, column=0)

facture_section_frame = Frame(frame_facture, bg="#64605A", width=350, height=458)
facture_section_frame.grid(row=1, column=0, padx=1, pady=1)
facture_section_frame.grid_propagate(0)

facture_totale_titre = Label(frame_facture, text="  TOTALE : 0$", anchor="w", fg="#D1D1D1", bg="#64605A", width=51, height=2)
facture_totale_titre.grid(row=5, column=0)

facture_bouton = tkinter.Button(frame_facture, text="commander", font=("Comic Sans MS", 12), bg="#C68E8E", fg="white", anchor="center", width=35, command=changer_a_au_revoir)
facture_bouton.grid(row=6, column=0, sticky="S", padx=2, pady=2)


# ----------------------------------------------D'autres images------------------------------------------------
banniere_image_objet = Image.open("Nourriture Stable.png").resize((1300, 500))
banniere_image = ImageTk.PhotoImage(banniere_image_objet)
banniere = Label(frame_banniere, image=banniere_image, height=250)
banniere.grid(row=0, column=1)

attendre_image_objet = Image.open("moyen_orient.jpg").resize((650, 492))
attendre_image = ImageTk.PhotoImage(attendre_image_objet)
attendre = Label(attendre_image_frame, image=attendre_image, width=500, height=365)
attendre.grid(row=0, column=0)

# Pour commencer la programme
win.mainloop()