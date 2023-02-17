from rest_framework import serializers
from app1.models import Patches

class PatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patches 
        fields=('PatcheId','col0','col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11','col12','col13','col14')
