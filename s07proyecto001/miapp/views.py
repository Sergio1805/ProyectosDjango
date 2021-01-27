from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Articulo
from miapp.models import Autor
from django.db.models import Q

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


def crear_articulo(request,titulo,contenido,publicado):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado,

    ) 
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")


def buscar_articulo(request,id):
    try:
        articulo = Articulo.objects.get(id=id)
        resultado = f"""Articulo: 
                    <br> <strong> ID:</Strong>{articulo.id}
                    <br> <strong> Titulo: </strong>{articulo.titulo}
                    <br> <strong> Contenido: </strong>{articulo.contenido}
                    """
    except:
        resultado = f"<h1> Articulo No Encontrado...</h1>"
    return HttpResponse(resultado)

def editar_articulo(request,id):
    articulo = Articulo.objects.get(pk=id)
    articulo.titulo = "Enseñanza online en la UNTELS"
    articulo.contenido = "Aula Virtual, Google Meet, Portal Académico, Google Classroom..."
    articulo.publicado=False

    articulo.save()
    return HttpResponse(f"Articulo Editado : {articulo.titulo}-{articulo.contenido}")

def listar_articulos(request):
    articulos = Articulo.objects.filter(
        Q(titulo__contains ="Py") |
        Q(titulo__contains ="Hab")  

    )
    return render(request, 'listar_articulos.html',{
        'articulos':articulos, 'titulo':'Listado de articulos'    
    })

def eliminar_articulo(request,id):
    articulo = Articulo.objects.all(pk=id)
    articulo.delete()
    return redirect('listar_articulos')

def save_articulo(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        if len(titulo)<=5:
            return HttpResponse("<h2>El tamaño del título es pequeño, intente nuevamente</h2>")
        contenido = request.POST['contenido']
        publicado = request.POST['publicado']

        articulo = Articulo(
            titulo = titulo,
            contenido = contenido,
            publicado = publicado
        )
        articulo.save()
        return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")
    else:
        return HttpResponse("<h2> No se ha podido registrar el artículo </h2>")




def create_articulo(resquest):
    return render(resquest, 'create_articulo.html')



#ddddddddddddddddddddddddddddddd
def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'listar_autores.html',{
        'autores':autores, 'titulo':'Listado de autores'    
    })

def eliminar_autor(request,id):
    autor = Autor.objects.get(pk=id)
    autor.delete()
    return redirect('listar_autores')

def save_autor(request): 
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        sexo = request.POST['sexo']
        Fecha_nacimiento=request.POST['Fecha_nacimiento']
        pais = request.POST['pais']

        autor = Autor(
            nombre = nombre,
            apellido = apellido,
            sexo = sexo,
            Fecha_nacimiento=Fecha_nacimiento,
            pais=pais

        )
        autor.save()
        return HttpResponse(f"Autor Creado: {autor.nombre} - {autor.apellido}- {autor.sexo}- {autor.Fecha_nacimiento}- {autor.pais}")
    else:
        return HttpResponse("<h2> No se ha podido registrar el autor </h2>")




def create_autor(resquest):
    return render(resquest, 'create_autor.html')

