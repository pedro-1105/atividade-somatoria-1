# IMC FORMULA :  peso / (altura X altura)


altura = float(input('qual é sua altura:'))
peso = float(input('qual é seu peso:'))
imc = peso / (altura * altura) 

resultado = round(imc, 2)

print(resultado)

if resultado <18.5:
    print('abaixo do peso')
    print('coma mais com cuidado')
elif resultado<24.9:
    print('peso normal')
    print('continue assim')
if resultado <29.9:
    print('Obesidade Grau I')
    print('coma legumes e se alimente com cautela ')
elif resultado<39.9:
    print('Obesidade Grau II')
    print('cuidado vc pode sofrer um ataque cardiaco')
else:
    print('Obesidade Grau III (mórbida)')
    print('coma verduras e frutas ou ira morrer no hospital')