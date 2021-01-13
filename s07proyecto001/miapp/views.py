from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    estudiantes = [
        'Sánchez Cárdenas Sergio',
        'Bendezu Santisteban Anthony',
        'Castillo Tordoya Gerardo',
        'Mansilla Menéndez Patrick'
                  ]
   
    return render(request, 'index.html', {
    'inicio': 'Inicio',
    'mensaje' : 'Proyecto web con Django (desde el view)',
    'estudiantes':estudiantes
    } )
def saludo(request):
    
    return render(request, 'saludo.html',{'saludo': 'Saludo',
    'nombre_autor' : 'Sergio Sánchez (desde el view)'
    } )

def rango(request):
    numeros=[]
    a =10
    a1=a
    b =20
    
    while a<=b:
        numeros.append(a)
        a+=1
    
    return render(request,'rango.html',{'rango':'Rango','a':a1,'b':b,'numeros':numeros})   


def rango2(request, a=0 ,b=100):
   
    resultado = f"""
                <h2> Rango con parámetros </h2>
                <h2> Números de [{a}] hasta [{b}] </h2>
                Resultado : <br>
                <ul>
    """
    if a>b:
        return redirect('rango2',a=b,b=a)

    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1

    resultado += "</ul>"
    return HttpResponse(resultado)   