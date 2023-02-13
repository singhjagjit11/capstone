from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from app1.models import Patches
from app1.serializers import PatchesSerializer

from django.core.files.storage import default_storage




from django.http import HttpResponse
from bs4 import BeautifulSoup

def get_html_content(request):
    import requests

    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.oracle.com/security-alerts/cpujan2023.html').text
    return html_content

@csrf_exempt
def loadPatchesApi(request,id=0):
    if request.method=='GET':
        # Fetch oracle data from https://www.oracle.com/security-alerts/cpujan2023.html
        html_content = get_html_content(request)
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table',class_="otable-w2")# Find the table
        






        objs = [Patches(Cve='Beatles Blog', Component='All the latest Beatles news.',BaseScore="555"), Patches(Cve='Beatles Blog', Component='All the latest Beatles news.',BaseScore="666")]
        Patches.objects.bulk_create(objs) 
        return JsonResponse("Added Successfully",safe=False)   
        # b = Patches(Cve='Beatles Blog', Component='All the latest Beatles news.',BaseScore="4")
        # b.save()

@csrf_exempt
def patchesApi(request,id=0):
    if request.method=='GET':
        patches = Patches.objects.all()
        patches_serializer=PatchesSerializer(patches,many=True)
        return JsonResponse(patches_serializer.data,safe=False)


    elif request.method=='POST':
        patches_data=JSONParser().parse(request)
        patches_serializer=PatchesSerializer(data=patches_data)
        if patches_serializer.is_valid():
            patches_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

