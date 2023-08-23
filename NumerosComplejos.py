import math
#Juan Sebastian Buitrago Piñeros
#Numeros Complejos y operaciones
def suma(a,b):
    parteR = a[0] + b[0]
    parteI = a[1] + b[1]
    return (parteR, parteI)

def producto(a,b):
    parteR = a[0] * a[1] - b[0] * b[1]
    parteI = b[0] * a[1] + b[1] * a[0] 
    return (parteR, parteI)

def resta(a,b):
    parteR = a[0] - a[1]
    parteI = b[0] - b[1]
    return (parteR, parteI)

def dividir(a, b):
    denominador = a[1]**2 + b[1]**2
    parteR = (a[0] * a[1] + b[0] * b[1]) / denominador
    parteI = (b[0] * a[1] - a[0] * b[1]) / denominador
    return (parteR, parteI)

def modulo(a, b):
    parte1 = ((a)**2 + (b)**2)**(1/2)
    return parte1

def conjugado(a, b):
    conjugado_imag = -b
    return (a,conjugado_imag)

def conversion_polar(a,b):
    p = ((a)**2 + (b)**2)**(1/2)
    angulo = math.atan(b/a)
    return (p, angulo)

def conversion_cartesiana(a,b):
    parteR = a*math.cos(b)
    parteI = a*math.sin(b)
    return (parteR, parteI)

def fase_numero_complejo(a, b):
    if a == 0 and b == 0:
        raise ValueError("El número complejo no tiene fase definida.")
    
    fase = math.atan2(a, b)
    return (fase)

#PARTE DE ENTREGA
#Archivo ".gitignore" (Archivo que describe que archivos dejar por fuera del control de versiones)
#No entendi, muy bien que archivos debo subir a github y donde los puedo subir

if __name__ == "__main__":
    print(suma((3,5),(-2.6,6.8)))
    print(producto((3,5),(-2.6,6.8))) 