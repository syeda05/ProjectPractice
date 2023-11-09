import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("key.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection('persons').add({'name':'John','age':40})   #autogenerated id
db.collection('persons').add({'name':'Rob','age':36})
db.collection('persons').document('joe').set({'name':'joe','age':69})    #manual id

db.collection('persons').document('joe').collection('movies').add({'name':'aaaa'})    #add sub-collection to a document