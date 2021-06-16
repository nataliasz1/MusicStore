import uuid

from django import forms
from django.core.files.storage import FileSystemStorage

from api.settings import DJANGO_FILES_FOLDER
from .fibase_config import storage
from .models import ProductImage, CatalogItem


class CatalogItemForm(forms.ModelForm):
    catalog_item_id = forms.ModelChoiceField(queryset=CatalogItem.objects.all())
    file = forms.FileField()

    class Meta:
        model = ProductImage
        fields = "__all__"

    def save(self, commit=True):
        file = self.cleaned_data.get('file')
        fs = FileSystemStorage(location=DJANGO_FILES_FOLDER)
        local_file = fs.save(file.name, file)
        unique_file_id = str(uuid.uuid4())
        storage.child(unique_file_id).put(fs.path(local_file))
        self.instance.file = unique_file_id
        fs.delete(local_file)
        return super().save(commit)
