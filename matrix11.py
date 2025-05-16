import pygame
import random
import sys


pygame.init()


largeur, hauteur = pygame.display.Info().current_w, pygame.display.Info().current_h
fenetre = pygame.display.set_mode((largeur, hauteur))


chiffres = [str(i) for i in range(10)]


taille_police = 35
police = pygame.font.SysFont("msgothic", taille_police)


colonnes = largeur // taille_police


gouttes = [random.randint(-20, 0) for _ in range(colonnes)]


vitesses = [random.choice([1, 1, 2, 2, 3]) for _ in range(colonnes)]


longueurs_trainées = [random.randint(5, 20) for _ in range(colonnes)]


trainées_vertes = []
for longueur in longueurs_trainées:
    trainées_vertes.append([random.choice(chiffres) for _ in range(longueur)])


fond = pygame.Surface((largeur, hauteur))
fond.set_alpha(100)  # fade léger
fond.fill((0, 0, 0))


VERT = (0, 255, 0)
BLANC = (255, 255, 255)


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fenetre.blit(fond, (0, 0))  # Effet de traînée

    for i in range(colonnes):
        x = i * taille_police
        y = gouttes[i] * taille_police

        
        char_blanc = random.choice(chiffres)
        texte_blanc = police.render(char_blanc, True, BLANC)
        fenetre.blit(texte_blanc, (x, y))

        
        longueur = longueurs_trainées[i]
        for j in range(1, longueur):
            y_vert = y - j * taille_police
            if y_vert >= 0 and j < len(trainées_vertes[i]):
                char_vert = trainées_vertes[i][j]
                texte_vert = police.render(char_vert, True, VERT)
                fenetre.blit(texte_vert, (x, y_vert))

        
        gouttes[i] += vitesses[i]

        
        if y > hauteur and random.random() > 0.98:
            gouttes[i] = random.randint(-20, 0)
            # Changer la longueur et la vitesse au redémarrage
            nouvelle_longueur = random.randint(5, 20)
            longueurs_trainées[i] = nouvelle_longueur
            vitesses[i] = random.choice([1, 1, 2, 2, 3])
            # Regénérer la trainée verte fixe pour cette colonne
            trainées_vertes[i] = [random.choice(chiffres) for _ in range(nouvelle_longueur)]

    pygame.display.update()
    clock.tick(15)
