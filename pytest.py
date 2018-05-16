#!/user/bin/python
import unittest
import DAO
import apiai
import texto
from pymongo import MongoClient



class TestDB(unittest.TestCase):
  '''
  def setUp(self):
     client = MongoClient('localhost',27017)
     dbUsuario = client.test.test
     return
  '''
  def test_insertar(self): 
     client = MongoClient('localhost',27017)
     dbUsuario = client.prueba.usuarios
     DAO.insertarNuevoUsuario(555)
     cursor = dbUsuario.find_one({'_id':555})
     self.assertTrue(cursor != 'None')

  def test_existeUsuario(self):
     client = MongoClient('localhost',27017)
     dbUsuario = client.prueba.usuarios
     self.assertTrue(DAO.existe_Usuario) 
      

  def test_getidioma(self):
     client = MongoClient('localhost',27017)
     dbUsuario = client.prueba.usuarios
     idioma = DAO.get_idioma(555)
     self.assertTrue(idioma =='Cast')
     dbUsuario.delete_one({'_id':555})
   
  def test_query(self):
     self.assertEqual(apiai.query("salario consejal",555,'Cast'),'un Concejal gana 66.495,37€ de retribución anual bruta (sin antigüedad)')
     self.assertEqual(apiai.query("salario Sergi",555,'Cast'),'Sergi Campillo Fernández gana 74.342,66€ de retribución anual bruta (sin antigüedad) por su cargo de Teniente de Alcalde.')
     self.assertEqual(apiai.query("impuesto benimaclet",555,'Cast'), 'el barrio Benimaclet pago en total 6.428.288,48 en impuestos el año 2016')
     self.assertEqual(apiai.query("ibi benimaclet 2018",555,'Cast'), 'no tenemos los impuesto del 2018 año. de momento solo contamos con los impuesto del año 2016')

  def test_addComa(self):
     self.assertEqual(DAO.addComa('78551.36'),'78.551,36')
     self.assertEqual(DAO.addComa(75585),'75.585')

  

if __name__== '__main__':
  unittest.main()
