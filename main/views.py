from django.shortcuts import render, HttpResponse, redirect
import random
import time

def index(request):
    return render(request, 'index.html')


def monedas(request):
    if 'logs' not in request.session:
            request.session['logs'] =[]
    if 'counter' in request.session:
        if request.POST['ninja'] == 'granja':
            farm = random.randint(0,10)
            print(farm)
            request.session['counter'] += farm
            datos= {
            'texto': f" Ganaste {farm } monedas en la granja -- {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}" ,
            'color': 'azul' if (farm >= 0)  else 'rojo' ,
            }
            request.session['logs'].append(datos)
            request.session.save()
            
        if request.POST['ninja'] == 'cueva':
            cave= random.randint(5,10)
            request.session['counter'] += cave
            datos= {
            'texto': f" Ganaste {cave } monedas en la cueva -- {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}" ,
             'color': 'azul' if (cave >= 0)  else 'rojo' ,
            }
            request.session['logs'].append(datos)
            request.session.save()
            print(request.session['counter'])
        if request.POST['ninja'] == 'casa':
            house=random.randint(2,5)
            request.session['counter'] += house
            datos= {
            'texto': f" Ganaste {house } monedas en la casa -- {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}" ,
             'color': 'azul' if (house >= 0)  else 'rojo' ,
            }
            request.session['logs'].append(datos)
            request.session.save()
            print(request.session['counter'])
        if request.POST['ninja'] == 'casino':
            casino= random.randint(-50,50)
            request.session['counter'] += casino
            datos= {
            'texto': 'Ganaste ' f"{casino} monedas en el casino -- {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}" if (casino >= 0)  else 'Perdiste ' f"{casino} monedas en el casino -- {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}" ,
            'color': 'azul' if (casino >= 0)  else 'rojo' ,
            }
            request.session['logs'].append(datos)
            request.session.save()
            print(request.session['counter'])
        

    else:
        request.session['counter'] = 0
        
    return redirect("/")

def resetear(request):
    if 'counter' in request.session:
        del request.session['counter']
    if 'logs' in request.session:
        del request.session['logs']
    return redirect("/")

