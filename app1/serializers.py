from rest_framework import serializers
from app1.models import Patches

class PatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patches 
        fields=('PatcheId','Cve','Component','BaseScore')
