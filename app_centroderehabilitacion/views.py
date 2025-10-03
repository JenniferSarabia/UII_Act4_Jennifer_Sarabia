from django.shortcuts import render

# Create your views here.
def index(request):
    pacientes = [
        {"nombre": "Ana Pérez", "edad": 35, "diagnostico": "Gripe"},
        {"nombre": "Juan García", "edad": 50, "diagnostico": "Hipertensión"},
        {"nombre": "María López", "edad": 28, "diagnostico": "Dolor de cabeza"},
    ]
    
    contexto = {
        'lista_pacientes': pacientes
    }
    
    return render(request, 'index.html', contexto)

