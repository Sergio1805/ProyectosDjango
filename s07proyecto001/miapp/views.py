from django.shortcuts import render, HttpResponse

# Create your views here.
layout = """
    <h1> Proyecto web (LP3) </h1>
    <h2> Sergio Sánchez </h2>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/saludo">Saludo</a>
        </li>
        <li>
            <a href="/rango">Mostrar números [a;b]</a>
        </li>
        <li>
            <a href="/rango2/10/20">Mostrar números(Parámetros) [a;b]</a>
        </li>
    </ul>
    <hr/>

"""
def index(request):
    mensaje = """
            <h1> INICIO </h1>

              """
    return HttpResponse(layout + mensaje)

def saludo(request):
    mensaje ="""
            <h1> Bienvenidos a la UNTELS </h1>
            <h2> FACULTAD DE INGENIERÍA <h2>
            <h3> INGENIERÍA DE SISTEMAS </h3>
            <h4> LP3 Flor Cerdán </h4>
            """
    return HttpResponse(layout + mensaje)

def rango(request):
    a =10
    b=20
    resultado = f"""
                <h2> Números de [{a}] hasta [{b}] </h2>
                Resultado : <br>
                <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1

    resultado += "</ul>"
    return HttpResponse(layout + resultado)   


def rango2(request, a,b):
   
    resultado = f"""
                <h2> Rango con parámetros </h2>
                <h2> Números de [{a}] hasta [{b}] </h2>
                Resultado : <br>
                <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1

    resultado += "</ul>"
    return HttpResponse(layout + resultado)   