#!/usr/bin/env/python
#datos presupestarios general..
#ayuntamiento valencia...
import requests
#from urllib.request import urlopen, urlretrieve
#from bs4 import BeautifulSoup as bs


gastos = ["GASTOS DE PERSONAL", "GASTOS CORRIENTES EN BIENES Y SERVICIOS","GASTOS FINANCIEROS","TRANSFERENCIAS CORRIENTES","INVERSIONES REALES", "TRANSFERENCIAS DE CAPITAL", "ACTIVOS FINANCIEROS", "PASIVOS FINANCIEROS","FONDO DE CONTINGENCIA Y OTROS IMPREVISTOS"]

def addComa(num):
  #need to be string to add coma
  i = num.index('.')
  while i > 3:
     i =i - 3
     num = num[:i] + ',' + num[i:]
  return num
def presupuesto_general():
  total = 0
  year = 2018
  page = requests.get("http://www.valencia.es:8070/somclars/sql/datos_presupuestarios/SELECT%20g.cuenta%2Cp.descripcion%2Cg.CredIniciales%20FROM%20gastos%20g%20JOIN%20planes_detalle%20p%20ON%20g.cuenta%3Dp.codigo%20AND%20g.plan%3Dp.plan%20WHERE%20g.plan%3D1%20AND%20ejercicio%3D{}%20ORDER%20BY%20cuenta%2Cp.descripcion%20ASC".format(year))

  if page.status_code == 200:
   
    presupuesto_datos = page.json()
    for i in range(0, len(presupuesto_datos[0]["data"])):
       if presupuesto_datos[0]["data"][i][1] in gastos:
        #print(presupuesto_datos[0]["data"][i][1], presupuesto_datos[0]["data"][i][2] )
        total += float(presupuesto_datos[0]["data"][i][2])
        #print("%0.2f" %total)
    return addComa(format(total,"0.2f"))

if __name__=='__main__':
   print(presupuesto_general())



