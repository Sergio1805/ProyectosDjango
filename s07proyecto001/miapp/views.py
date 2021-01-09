from django.shortcuts import render, HttpResponse, redirect

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
            <a href="/rango2">Mostrar números(Parámetros) [a;b]</a>
        </li>
    </ul>
    <hr/>

"""
def index(request):
   
    return render(request, 'index.html')

def saludo(request):
    
    return render(request, 'saludo.html')

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
    return HttpResponse(layout + resultado)   