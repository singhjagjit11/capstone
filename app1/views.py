from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from app1.models import Patches
from app1.serializers import PatchesSerializer

from django.core.files.storage import default_storage
import requests



from django.http import HttpResponse
from bs4 import BeautifulSoup


@csrf_exempt
def loadPatchesApi(request,id=0):
    if request.method=='GET':
        # # Fetch oracle data from https://www.oracle.com/security-alerts/cpujan2023.html
        # html_content = get_html_content(request)
        # soup = BeautifulSoup(html_content, 'html.parser')


        url = "https://www.oracle.com/security-alerts/cpujan2023.html"

        # send a request to the URL
        response = requests.get(url)

        # parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")
        
        #table = soup.find('table',class_="otable-w2")# Find the table
        tables = soup.find_all("table")
        table = tables[2]
        # find the tbody in the table
        tbody = table.find("tbody")
        rows = tbody.find_all("tr")# extract the rows from the tbody
       

        objs=[]
        for row in rows:
            cells = row.find_all("td")
            cells2 = row.find_all("th")
            data2 = [cell.text for cell in cells2]
            data = [cell.text for cell in cells]
            data =[*data2,*data]
            print(data)

            objs.append(Patches(col0=data[0], col1=data[1],col2=data[2],col3=data[3], col4=data[4],col5=data[5],col6=data[6],
             col7=data[7],col8=data[8],col9=data[9], col10=data[10],col11=data[11],col12=data[12],col13=data[13], col14=data[14]))
            

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

    #for testing
    elif request.method=='POST':
        patches_data=JSONParser().parse(request)
        patches_serializer=PatchesSerializer(data=patches_data)
        if patches_serializer.is_valid():
            patches_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

def disp(request):
    response=requests.get('http://127.0.0.1:8000/patch').json()
    return render(request,'index.html',{'response':response})