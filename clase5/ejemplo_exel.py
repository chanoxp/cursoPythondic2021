import pandas as pd
import openpyxl


leer_fichero = pd.read_csv(r'./catalogo_cf2.csv')
leer_fichero.to_excel(r'./catalogo_cf2.xlsx', index=None, header=True)