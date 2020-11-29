#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:20:12 2020

@author: Egidio
"""
import numpy as np
import networkx as nx 

# Il modello di Erdos-Renyi è un modello per la generazione di reti casuali.
# Si implementa un algoritmo per la generazione di un semplice grafo che ha un
# solo arco tra i nodi e non presenta autolink.
n = 10 # numero di nodi 
p = 0.3 # probabilità di connessione

# Si crea una matrice di soli zeri
A=np.zeros((n,n))

# Gli indici
i=0
j=0

# Nella matrice A si scorrono prima le righe e poi le colonne. Quindi se
# il numero generato randomicamente r è minore della probabilità di 
# connessione p e gli indcici i e j sono diversi, si assegna un 1 nella
# posizione indicata dagli indici. Nel caso di indici uguali si mantiene lo 
# 0, anche se è verificata la condizione r<p, perchè il grafo sia semplice.
for riga in A:
    for colonna in riga:    
        r = np.random.random(1)[0]
        if r < p:
            if i!=j:
                A[i][j]= 1
                A[j][i]= 1
            elif i==j:
                A[i][j]= 0 # non si vogliono autolink
        j += 1
    j=0
    i+=1

# Si costruisce un grafo dalla matrice A che si considera come matrice di
# adiacenza
G = nx.from_numpy_matrix(A)

# Si plotta il grafo
nx.draw(G, with_labels=1)