# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as alea




def visu_point(matPoint, style):
    # matPoint contient les coordonnées des points
    x = matPoint[0, :]
    y = matPoint[1, :]
    plt.plot(x, y, style)

def visu_segment(P1, P2, style):
    # attention P1 et P2 sont des tableaux (2,1)
    matP = np.concatenate((P1, P2), 1)
    visu_point(matP, style)

def mat_rotation(theta):
    # si pas besoin des coordonnées homogènes
    mat = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])
    return mat



# FONCTION BÉZIER CUBIQUE

def courbe_Bezier_cubique(P0, P1, P2, P3):

    n = 100
    t = np.linspace(0, 1, n)

    mat_t = np.ones((4, n))
    mat_t[1, :] = t
    mat_t[2, :] = t*t
    mat_t[3, :] = t*t*t

    matBezier4 = np.array([
        [1, 0, 0, 0],
        [-3, 3, 0, 0],
        [3, -6, 3, 0],
        [-1, 3, -3, 1]
    ])

    matPointControl = np.array([P0, P1, P2, P3])

    matPointligne = (mat_t.T @ matBezier4) @ matPointControl
    matPoint = matPointligne.T

    x = matPoint[0, :]
    y = matPoint[1, :]

    return x, y

# DÉCORATIONS

def decorations():

    # arbres
    plt.plot(60, 320, "go", markersize=18)
    plt.plot(60, 305, "ks", markersize=5)

    plt.plot(100, 300, "go", markersize=14)
    plt.plot(100, 287, "ks", markersize=5)

    plt.plot(320, 320, "go", markersize=15)
    plt.plot(320, 307, "ks", markersize=5)

    # buissons
    plt.plot(80, 80, "go", markersize=12)
    plt.plot(95, 95, "go", markersize=8)
    plt.plot(60, 100, "go", markersize=7)

    plt.plot(340, 90, "go", markersize=10)
    plt.plot(360, 70, "go", markersize=7)

    # panneau
    plt.plot(90, 210, "ks", markersize=5)
    plt.plot(90, 230, "ro", markersize=12)

    plt.text(
        90,
        230,
        "90",
        ha="center",
        va="center",
        color="white",
        fontsize=8
    )

    # cailloux
    plt.plot(50, 250, "ko", markersize=4)
    plt.plot(70, 260, "ko", markersize=3)
    plt.plot(300, 60, "ko", markersize=4)







# TUILE VIRAGE

def tuile_virage(nouvelle_figure=True):

    taille = 400

    if nouvelle_figure:
        plt.figure(figsize=(7, 7))

    # fond herbe
    plt.fill(
        [0, taille, taille, 0],
        [0, 0, taille, taille],
        color="lightgreen"
    )

    # contour
    plt.plot(
        [0, taille, taille, 0, 0],
        [0, 0, taille, taille, 0],
        "k",
        linewidth=3
    )



    # bord gauche
    P0 = np.array([150, 0])
    P1 = np.array([147.5, 147.5])
    P2 = np.array([247.5, 247.5])
    P3 = np.array([400, 250])

    x1, y1 = courbe_Bezier_cubique(P0, P1, P2, P3)

    # bord droit
    P0b = np.array([250, 0])
    P1b = np.array([250, 100])
    P2b = np.array([300, 150])
    P3b = np.array([400, 150])

    x2, y2 = courbe_Bezier_cubique(P0b, P1b, P2b, P3b)

    # remplir route
    x_route = np.concatenate((x1, x2[::-1]))
    y_route = np.concatenate((y1, y2[::-1]))

    plt.fill(x_route, y_route, color="gray")

    # bordures
    visu_point(np.array([x1, y1]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x2, y2]), "k")
    plt.gca().lines[-1].set_linewidth(3)

    # ligne du milieu
    P0m = np.array([200, 0])
    P1m = np.array([200, 125])
    P2m = np.array([275, 200])
    P3m = np.array([400, 200])

    xm, ym = courbe_Bezier_cubique(P0m, P1m, P2m, P3m)

    visu_point(np.array([xm, ym]), "w--")
    plt.gca().lines[-1].set_linewidth(3)

    # décorations
    decorations()

    # affichage
    plt.axis("equal")
    plt.xlim(0, taille)
    plt.ylim(0, taille)
    plt.grid()




# TUILE DROITE
def tuile_droite(nouvelle_figure=True):

    taille = 400

    if nouvelle_figure:
        plt.figure(figsize=(7, 7))

    # fond herbe
    plt.fill(
        [0, taille, taille, 0],
        [0, 0, taille, taille],
        color="lightgreen"
    )

    # contour
    plt.plot(
        [0, taille, taille, 0, 0],
        [0, 0, taille, taille, 0],
        "k",
        linewidth=3
    )


    # route
    plt.fill(
        [150, 250, 250, 150],
        [0, 0, 400, 400],
        color="gray"
    )

    # bordures
    visu_segment(np.array([[150], [0]]), np.array([[150], [400]]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_segment(np.array([[250], [0]]), np.array([[250], [400]]), "k")
    plt.gca().lines[-1].set_linewidth(3)

    # ligne blanche milieu
    visu_segment(np.array([[200], [0]]), np.array([[200], [400]]), "w--")
    plt.gca().lines[-1].set_linewidth(3)

    # décorations
    decorations()

    # affichage
    plt.axis("equal")
    plt.xlim(0, taille)
    plt.ylim(0, taille)
    plt.grid()
    
    
    
    
# TUILE Droite Quadruple Chemin
def tuile_Droite_Quadruple_chemin(nouvelle_figure=True):

    taille = 400

    if nouvelle_figure:
        plt.figure(figsize=(7, 7))

    # fond herbe
    plt.fill(
        [0, taille, taille, 0],
        [0, 0, taille, taille],
        color="lightgreen"
    )

    # contour
    plt.plot(
        [0, taille, taille, 0, 0],
        [0, 0, taille, taille, 0],
        "k",
        linewidth=3
    )


    #ligne en bas/gauche
    P0a = np.array([150, 0])
    P1a = np.array([150, 25])
    P2a = np.array([150,25])
    P3a = np.array([150, 150])
    x1, y1 = courbe_Bezier_cubique(P0a, P1a, P2a, P3a)

    #ligne en bas/droite
    P0b = np.array([250, 0])
    P1b = np.array([250, 75])
    P2b = np.array([250, 75])
    P3b = np.array([250, 150])
    x2, y2 = courbe_Bezier_cubique(P0b, P1b, P2b, P3b)
    
    #ligne en haut/gauche
    P0c = np.array([150, 400])
    P1c = np.array([150, 325])
    P2c = np.array([150,325])
    P3c = np.array([150, 250])
    x3, y3 = courbe_Bezier_cubique(P0c, P1c, P2c, P3c)

    #ligne en haut/droite
    P0d = np.array([250, 400])
    P1d = np.array([250, 325])
    P2d = np.array([250, 325])
    P3d = np.array([250, 250])
    x4, y4 = courbe_Bezier_cubique(P0d, P1d, P2d, P3d)
    
    
    
    
    #ligne-coter en bas/gauche
    P0a = np.array([0, 150])
    P1a = np.array([75, 150])
    P2a = np.array([75,150])
    P3a = np.array([150, 150])
    x5, y5 = courbe_Bezier_cubique(P0a, P1a, P2a, P3a)

    #ligne-coter en bas/droite
    P0b = np.array([250, 150])
    P1b = np.array([325, 150])
    P2b = np.array([325, 150])
    P3b = np.array([400, 150])
    x6, y6 = courbe_Bezier_cubique(P0b, P1b, P2b, P3b)
    
    #ligne-coter en haut/gauche
    P0c = np.array([250, 250])
    P1c = np.array([325, 250])
    P2c = np.array([325,250])
    P3c = np.array([400, 250])
    x7, y7 = courbe_Bezier_cubique(P0c, P1c, P2c, P3c)

    #ligne-coter en haut/droite
    P0d = np.array([150, 250])
    P1d = np.array([75, 250])
    P2d = np.array([75, 250])
    P3d = np.array([0, 250])
    x8, y8 = courbe_Bezier_cubique(P0d, P1d, P2d, P3d)
    
    
    
    
    
    
    
    
    
    
    
    
    
    # les ligne du milieu
    P0ma = np.array([200, 0])
    P1ma = np.array([200, 200])
    P2ma = np.array([200, 200])
    P3ma = np.array([200, 400])
    xm, ym = courbe_Bezier_cubique(P0ma, P1ma, P2ma, P3ma)
    visu_point(np.array([xm, ym]), "w--")
    plt.gca().lines[-1].set_linewidth(3)
    
   
    P0md = np.array([400, 200])
    P1md = np.array([200, 200])
    P2md = np.array([200, 200])
    P3md = np.array([0, 200])
    xm, ym = courbe_Bezier_cubique(P0md, P1md, P2md, P3md)
    visu_point(np.array([xm, ym]), "w--")
    plt.gca().lines[-1].set_linewidth(3)
    
    
    
    # route complète
        # route verticale
    plt.fill(
        [150, 250, 250, 150],
        [0, 0, 400, 400],
        color="gray"
    )
    
    # route horizontale
    plt.fill(
        [0, 400, 400, 0],
        [150, 150, 250, 250],
        color="gray"
    )


    

    # bordures
    visu_point(np.array([x1, y1]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x2, y2]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x3, y3]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x4, y4]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x5, y5]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x6, y6]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x7, y7]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x8, y8]), "k")
    plt.gca().lines[-1].set_linewidth(3)



    # arbres
    plt.plot(60, 320, "go", markersize=18)
    plt.plot(60, 305, "ks", markersize=5)

    plt.plot(100, 300, "go", markersize=14)
    plt.plot(100, 287, "ks", markersize=5)

    plt.plot(320, 320, "go", markersize=15)
    plt.plot(320, 307, "ks", markersize=5)

    # buissons
    plt.plot(80, 80, "go", markersize=12)
    plt.plot(95, 95, "go", markersize=8)
    plt.plot(60, 100, "go", markersize=7)

    plt.plot(340, 90, "go", markersize=10)
    plt.plot(360, 70, "go", markersize=7)



    # cailloux
    plt.plot(50, 270, "ko", markersize=4)
    plt.plot(70, 280, "ko", markersize=3)
    plt.plot(300, 60, "ko", markersize=4)

    # affichage
    plt.axis("equal")
    plt.xlim(0, taille)
    plt.ylim(0, taille)
    plt.grid()          
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# TUILE Quadruple Chemin
def tuile_Quadruple_chemin(nouvelle_figure=True):

    taille = 400

    if nouvelle_figure:
        plt.figure(figsize=(7, 7))

    # fond herbe
    plt.fill(
        [0, taille, taille, 0],
        [0, 0, taille, taille],
        color="lightgreen"
    )

    # contour
    plt.plot(
        [0, taille, taille, 0, 0],
        [0, 0, taille, taille, 0],
        "k",
        linewidth=3
    )


    #courbe en bas/gauche
    P0a = np.array([150, 0])
    P1a = np.array([150, 100])
    P2a = np.array([100,150])
    P3a = np.array([0, 150])
    x1, y1 = courbe_Bezier_cubique(P0a, P1a, P2a, P3a)

    #courbe en bas/droite
    P0b = np.array([250, 0])
    P1b = np.array([250, 100])
    P2b = np.array([300, 150])
    P3b = np.array([400, 150])
    x2, y2 = courbe_Bezier_cubique(P0b, P1b, P2b, P3b)
    
    #courbe en haut/gauche
    P0c = np.array([150, 400])
    P1c = np.array([150, 300])
    P2c = np.array([100,250])
    P3c = np.array([0, 250])
    x3, y3 = courbe_Bezier_cubique(P0c, P1c, P2c, P3c)

    #courbe en haut/droite
    P0d = np.array([250, 400])
    P1d = np.array([250, 300])
    P2d = np.array([300, 250])
    P3d = np.array([400, 250])
    x4, y4 = courbe_Bezier_cubique(P0d, P1d, P2d, P3d)
    
    
    
    # les courbe noir du milieu
    P0na = np.array([160, 200])
    P1na = np.array([180, 210])
    P2na = np.array([190,220])
    P3na = np.array([200, 240])
    x5, y5 = courbe_Bezier_cubique(P0na, P1na, P2na, P3na)

    #courbe en bas/droite
    P0nb = np.array([200, 160])
    P1nb = np.array([210, 180])
    P2nb = np.array([220, 190])
    P3nb = np.array([240, 200])
    x6, y6 = courbe_Bezier_cubique(P0nb, P1nb, P2nb, P3nb)
    
    #courbe en haut/gauche
    P0nc = np.array([240, 200])
    P1nc = np.array([220, 210])
    P2nc = np.array([210,220])
    P3nc = np.array([200, 240])
    x7, y7 = courbe_Bezier_cubique(P0nc, P1nc, P2nc, P3nc)

    #courbe en haut/droite
    P0nd = np.array([200, 160])
    P1nd = np.array([190, 180])
    P2nd = np.array([180, 190])
    P3nd = np.array([160, 200])
    x8, y8 = courbe_Bezier_cubique(P0nd, P1nd, P2nd, P3nd)
    
    
    
    
    
    
    
    # les ligne du milieu
    P0ma = np.array([200, 0])
    P1ma = np.array([200, 125])
    P2ma = np.array([275, 200])
    P3ma = np.array([400, 200])
    xm, ym = courbe_Bezier_cubique(P0ma, P1ma, P2ma, P3ma)
    visu_point(np.array([xm, ym]), "w--")
    plt.gca().lines[-1].set_linewidth(3)
    
    P0mb = np.array([200, 0])
    P1mb = np.array([200, 125])
    P2mb = np.array([125, 200])
    P3mb = np.array([0, 200])
    xm, ym = courbe_Bezier_cubique(P0mb, P1mb, P2mb, P3mb)
    visu_point(np.array([xm, ym]), "w--")
    plt.gca().lines[-1].set_linewidth(3)
    
    P0mc = np.array([200, 400])
    P1mc = np.array([200, 275])
    P2mc = np.array([275, 200])
    P3mc = np.array([400, 200])
    xm, ym = courbe_Bezier_cubique(P0mc, P1mc, P2mc, P3mc)
    visu_point(np.array([xm, ym]), "w--")
    plt.gca().lines[-1].set_linewidth(3)
    
    P0md = np.array([200, 400])
    P1md = np.array([200, 275])
    P2md = np.array([125, 200])
    P3md = np.array([0, 200])
    xm, ym = courbe_Bezier_cubique(P0md, P1md, P2md, P3md)
    visu_point(np.array([xm, ym]), "w--")
    plt.gca().lines[-1].set_linewidth(3)
    
    
    # route complète
    plt.fill(
        np.concatenate((x1, x3[::-1], x4, x2[::-1])),
        np.concatenate((y1, y3[::-1], y4, y2[::-1])),
        color="gray"
    )
    
    # trou vert central
    plt.fill(
        np.concatenate((x5, x7[::-1], x6[::-1], x8)),
        np.concatenate((y5, y7[::-1], y6[::-1], y8)),
        color="lightgreen"
    )


   
    

    # bordures
    visu_point(np.array([x1, y1]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x2, y2]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x3, y3]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x4, y4]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x5, y5]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x6, y6]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x7, y7]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x8, y8]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    



    # affichage
    plt.axis("equal")
    plt.xlim(0, taille)
    plt.ylim(0, taille)
    plt.grid()      
    
    
    
    

# TUILE triple Chemin
def tuile_triple_chemin(nouvelle_figure=True):

    taille = 400

    if nouvelle_figure:
        plt.figure(figsize=(7, 7))

    # fond herbe
    plt.fill(
        [0, taille, taille, 0],
        [0, 0, taille, taille],
        color="lightgreen"
    )

    # contour
    plt.plot(
        [0, taille, taille, 0, 0],
        [0, 0, taille, taille, 0],
        "k",
        linewidth=3
    )


    #courbe en bas/gauche
    P0a = np.array([150, 0])
    P1a = np.array([150, 100])
    P2a = np.array([100,150])
    P3a = np.array([0, 150])
    x1, y1 = courbe_Bezier_cubique(P0a, P1a, P2a, P3a)

    #courbe en bas/droite
    P0b = np.array([250, 0])
    P1b = np.array([250, 100])
    P2b = np.array([300, 150])
    P3b = np.array([400, 150])
    x2, y2 = courbe_Bezier_cubique(P0b, P1b, P2b, P3b)
    

    
    
    
   
    #courbe en bas/droite
    P0nb = np.array([200, 160])
    P1nb = np.array([225, 215])
    P2nb = np.array([275, 250])
    P3nb = np.array([400, 250])
    x6, y6 = courbe_Bezier_cubique(P0nb, P1nb, P2nb, P3nb)
    
   

    #courbe en haut/droite
    P0nd = np.array([200, 160])
    P1nd = np.array([175, 215])
    P2nd = np.array([125, 250])
    P3nd = np.array([0, 250])
    x8, y8 = courbe_Bezier_cubique(P0nd, P1nd, P2nd, P3nd)
    
    
    
    
    # route complète
    plt.fill(
        np.concatenate((x1, x8[::-1], x6, x2[::-1])),
        np.concatenate((y1, y8[::-1], y6, y2[::-1])),
        color="gray"
    )
    

    
    
    # les ligne du milieu
    P0ma = np.array([200, 0])
    P1ma = np.array([200, 125])
    P2ma = np.array([275, 200])
    P3ma = np.array([400, 200])
    xm, ym = courbe_Bezier_cubique(P0ma, P1ma, P2ma, P3ma)
    visu_point(np.array([xm, ym]), "w--")
    plt.gca().lines[-1].set_linewidth(3)
    
    P0mb = np.array([200, 0])
    P1mb = np.array([200, 125])
    P2mb = np.array([125, 200])
    P3mb = np.array([0, 200])
    xm, ym = courbe_Bezier_cubique(P0mb, P1mb, P2mb, P3mb)
    visu_point(np.array([xm, ym]), "w--")
    plt.gca().lines[-1].set_linewidth(3)
    


    # bordures
    visu_point(np.array([x1, y1]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x2, y2]), "k")
    plt.gca().lines[-1].set_linewidth(3)

    visu_point(np.array([x6, y6]), "k")
    plt.gca().lines[-1].set_linewidth(3)
  
    visu_point(np.array([x8, y8]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    



    # arbres
    plt.plot(60, 320, "go", markersize=18)
    plt.plot(60, 305, "ks", markersize=5)

    plt.plot(100, 300, "go", markersize=14)
    plt.plot(100, 287, "ks", markersize=5)

    plt.plot(320, 320, "go", markersize=15)
    plt.plot(320, 307, "ks", markersize=5)

    # buissons
    plt.plot(80, 80, "go", markersize=12)
    plt.plot(95, 95, "go", markersize=8)
    plt.plot(60, 100, "go", markersize=7)

    plt.plot(340, 90, "go", markersize=10)
    plt.plot(360, 70, "go", markersize=7)



    # cailloux
    plt.plot(50, 270, "ko", markersize=4)
    plt.plot(70, 280, "ko", markersize=3)
    plt.plot(300, 60, "ko", markersize=4)

    # affichage
    plt.axis("equal")
    plt.xlim(0, taille)
    plt.ylim(0, taille)
    plt.grid()  
    
    
# TUILE ROND
def tuile_ROND(nouvelle_figure=True):

    taille = 400

    if nouvelle_figure:
        plt.figure(figsize=(7, 7))

    # fond herbe
    plt.fill(
        [0, taille, taille, 0],
        [0, 0, taille, taille],
        color="lightgreen"
    )

    # contour
    plt.plot(
        [0, taille, taille, 0, 0],
        [0, 0, taille, taille, 0],
        "k",
        linewidth=3
    )


   
    P0a = np.array([200, 115])
    P1a = np.array([30, 300])
    P2a = np.array([370, 300])
    P3a = np.array([200, 115])
    x1, y1 = courbe_Bezier_cubique(P0a, P1a, P2a, P3a)

    P0b = np.array([250, 0])
    P1b = np.array([700, 478])
    P2b = np.array([-300, 478])
    P3b = np.array([150, 0])
    x2, y2 = courbe_Bezier_cubique(P0b, P1b, P2b, P3b)
    
    
    
    plt.fill(
        np.concatenate((x2, x1[::-1])),
        np.concatenate((y2, y1[::-1])),
        color="gray"
    )
    
    # remplir le triangle vert du bas
    plt.fill(
        [150, 200, 250],
        [0, 115, 0],
        color="gray"
    )
    
    # intérieur vert
    plt.fill(x1, y1, color="lightgreen")
    

    # bordures
    visu_point(np.array([x1, y1]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    visu_point(np.array([x2, y2]), "k")
    plt.gca().lines[-1].set_linewidth(3)
    
    
    #ligne blanche
    P0ma = np.array([200, 25])
    P1ma = np.array([570, 410])
    P2ma = np.array([-170, 410])
    P3ma = np.array([200, 25])
    xm, ym = courbe_Bezier_cubique(P0ma, P1ma, P2ma, P3ma)
    visu_point(np.array([xm, ym]), "w--")
    plt.gca().lines[-1].set_linewidth(3)
    
    
    #2eme ligne blanche
    P0ma = np.array([200, 0])
    P1ma = np.array([200, 15])
    P2ma = np.array([200, 15])
    P3ma = np.array([200, 25])
    xm, ym = courbe_Bezier_cubique(P0ma, P1ma, P2ma, P3ma)
    visu_point(np.array([xm, ym]), "w--")
    plt.gca().lines[-1].set_linewidth(3)
    
    

    # affichage
    plt.axis("equal")
    plt.xlim(0, taille)
    plt.ylim(0, taille)
    plt.grid()    
    
    
def tilemap_aleatoire():

    liste_tuiles = [
        tuile_virage,
        tuile_droite,
        tuile_Droite_Quadruple_chemin,
        tuile_triple_chemin,
        tuile_Quadruple_chemin,
        tuile_ROND
    ]

    fig, axes = plt.subplots(5, 5, figsize=(10, 10))

    fig.subplots_adjust(
        left=0,
        right=1,
        bottom=0,
        top=1,
        wspace=0,
        hspace=0
    )

    for i in range(5):
        for j in range(5):

            plt.sca(axes[i, j])
            tuile = alea.choice(liste_tuiles)
            tuile(nouvelle_figure=False)

            # rotation aléatoire de l'affichage
            angle = alea.choice([0, 90, 180, 270])
            theta = np.deg2rad(angle)
            R = mat_rotation(theta)
            point_test = np.array([[1], [0]])
            point_rot = R @ point_test

            plt.gca().set_title("")
            plt.gca().set_aspect("equal")

            if angle == 90:
                plt.gca().invert_xaxis()
                plt.gca().set_xlim(400, 0)
                plt.gca().set_ylim(0, 400)

            elif angle == 180:
                plt.gca().invert_xaxis()
                plt.gca().invert_yaxis()

            elif angle == 270:
                plt.gca().invert_yaxis()
                plt.gca().set_xlim(0, 400)
                plt.gca().set_ylim(400, 0)

            plt.grid(False)
            plt.xticks([])
            plt.yticks([])

    plt.show()

#affichage
tuile_virage()
tuile_droite()
tuile_Droite_Quadruple_chemin()
tuile_triple_chemin()
tuile_Quadruple_chemin()
tuile_ROND()


tilemap_aleatoire()
