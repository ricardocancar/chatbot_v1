#!/usr/bin/python
from pymongo import MongoClient
import re



client = MongoClient("localhost",27017)
db = client.datos_valencia


regx = re.compile("^María", re.IGNORECASE)
marias=list(db.salarios.find({"nombre": regx}))
print(len(marias))
