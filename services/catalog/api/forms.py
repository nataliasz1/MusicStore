from django import forms
import os
import pyrebase
from api.settings import BASE_DIR
import json

from .models import ProductImage, CatalogItem

from .settings import FIREBASE_CONFIG_FILE

conf = ''

FIREBASE_FILE_PATH = os.path.join(BASE_DIR, FIREBASE_CONFIG_FILE)
with open(FIREBASE_FILE_PATH, "r") as read_file:
    j = json.load(read_file)

config = j
firebase = pyrebase.initialize_app(config)
#storageRef = firebase.storage().ref()

class MyProductImage(forms.ModelForm):
    image_id = forms.IntegerField()
    catalog_item_id = forms.ModelChoiceField(queryset=CatalogItem.objects.all())
       
    
    file = forms.FileField()

    #def save(self, file):
        
       # storageRef.child('images/mountains.jpg').put(file)

    class Meta:
        model = ProductImage
        fields = "__all__"
