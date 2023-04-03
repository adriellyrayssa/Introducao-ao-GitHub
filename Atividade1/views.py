from django.shortcuts import render, redirect
from django.contrib import messages

def Atividade1(request):
    if request.method == "GET":
        return render(request, "Atividade1.html")
    elif request.method == "POST":
        DNA = request.POST.get('DNA')
        if not DNA:
            # Criar uma mensagem de erro
            mensagem_de_erro = "Erro: A sequência de DNA informada está vazia."
            # Armazenar a mensagem de erro na sessão flash
            messages.error(request, mensagem_de_erro)
            # Redirecionar para a página de erro

        contadora = 0
        contadorg = 0
        contadorc = 0
        contadort = 0

        string = ""
        for i in DNA:
            if i == "A":
                contadora = contadora + 1
                string += "T"
            elif i == "G":
                contadorg = contadorg + 1
                string += "C"
            elif i == "C":
                contadorc = contadorc + 1
                string += "G"
            elif i == "T":
                contadort = contadort + 1
                string += "A"
            else:
                messages.error(request, f" Erro: A sequência de DNA informada contém caracteres inválidos")
                break

        context = {
            'num_Adenina': contadora,
            'num_Guanina': contadorg,
            'num_Citosina': contadorc,
            'num_Timina': contadort,
            'nova_string': string,
            'string': DNA,
        }

        return render(request, "Atividade1.html", context=context)
