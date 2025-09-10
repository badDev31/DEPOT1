import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.histogram(données, x='produit', y='prix', color='produit', title='chiffre par produit')

figure.write_html('chiffre-par-produit.html')

print('chiffre-par-produit.html généré avec succès !')
