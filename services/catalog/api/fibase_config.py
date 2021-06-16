import pyrebase as pyrebase

config = {
    "apiKey": "AIzaSyAetpe2HOP3s1JJsGoUbGnmW1dCsPvXYUA",
    "authDomain": "music-store-51f5c.firebaseapp.com",
    "projectId": "music-store-51f5c",
    "storageBucket": "music-store-51f5c.appspot.com",
    "messagingSenderId": "194327905906",
    "appId": "1:194327905906:web:73c3652b7528803aa5e4eb",
    "measurementId": "G-XHJH9T1Z3J",
    "databaseURL": ''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()
