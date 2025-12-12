from django.shortcuts import render
def mileage(request):
    distance = int(request.POST.get('distance', '0'))
    fuel_consumed = int(request.POST.get('fuel_consumed', '1'))
    mileage = distance/fuel_consumed if request.method == 'POST' else 0
    print("distance=",distance)
    print("fuel_consumed=",fuel_consumed)
    print("mileage=",mileage)
    return render(request, 'mathapp/math.html', {'distance': distance, 'fuel_consumed': fuel_consumed, 'mileage': mileage})
