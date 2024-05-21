from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import redirect

lenguajes = [
    ["Python", "C++", "PHP"],
    ["Python", "C++", "PHP"],
    ["Python", "C++", "PHP"],
    ["Python", "C++", "PHP"],
    ["Python", "C++", "PHP"],
]

# Request: Peticion
# HttpResponse: Respuesta en HTTP 

# Primera vista
def bienvenida(request): # Objeto de tipo request como primer argumento
    return HttpResponse("Bienvenid@ a su proyecto Django")

def sumarNumeros(request):
    numero_uno = 2
    numero_dos = 2
    suma = numero_uno + numero_dos
    resultado = "<h1>La suma de los dos números es: %s</h1>" %suma
    return HttpResponse(resultado)

def primeraPlantilla(request): 
    return render(request, 'primeraPlantilla.html', {"lenguajes" : lenguajes})

# Método para retornar el template
def plantillaAgregarElemento(request):
    return render(request, 'agregarElemento.html')

# Método para agregar a la lista
def agregarElemento(request):
    nombre = request.POST.get('nombre')
    anio = request.POST.get('anio')
    descargas = request.POST.get('descargas')
    nuevo_registro = [nombre, anio, descargas]
    lenguajes.append(nuevo_registro)
    return redirect('primera_plantilla')  # Redirecciona a la página principal

# Método para eliminar el último elemento de la lista
def eliminarElemento(request):
    lenguajes.pop()
    # lenguajes = lenguajes[:-1]
    return redirect('primera_plantilla')  # Redirecciona a la página principal
