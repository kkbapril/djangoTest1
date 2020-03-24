from django.shortcuts import render,redirect
from .models import Save_place

# Create your views here.
def map(request):
    if request.method == 'POST':
        print("POST request")
        print(float(request.POST['lat']))

        register = request.POST['register']
        place_name = request.POST['place_name']
        lat = float(request.POST['lat'])
        lng = float(request.POST['lng'])
        road_address = request.POST['road_address']
        jibun_address = request.POST['jibun_address']
        phone = request.POST['phone']
        category = request.POST['category']

        new_place = Save_place.objects.create(
            register=register, place_name=place_name, lat=lat, lng=lng
            ,road_address=road_address,jibun_address=jibun_address,phone=phone,category=category
        )
        return redirect('/map')
    elif request.method == 'GET':
        print("GET request")
        placeList = Save_place.objects.order_by()
        return render(request, 'second/map.html', {'places': placeList})

def map_list(request):
    placeList = Save_place.objects.order_by()
    return render(request, 'second/map.html', {'places': placeList})
