import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')
# 1) Agréger les quantités par produit
ventes_par_produit = (données
    .groupby('produit', as_index=False)['qte']
    .sum()
    .sort_values('qte', ascending=False)
)

# 1-bis) Graphe barres : ventes par produit (quantité)
fig1 = px.bar(
    ventes_par_produit,
    x='produit', y='qte',
    title='Ventes par produit (quantité)'
)
fig1.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré')

# C) CA par produit (prix * qte)
données['ca'] = données['prix'] * données['qte']
ca_par_produit = (données
    .groupby('produit', as_index=False)['ca']
    .sum()
    .sort_values('ca', ascending=False)
)
fig2 = px.bar(ca_par_produit, x='produit', y='ca', title="Chiffre d'affaires par produit")
fig2.write_html('ca-par-produit.html')
print('ca-par-produit.html généré')