altura = float(input('qual a sua altura em cm: '))
peso = float(input('qual seu peso em kg: '))

IMC = peso / (altura/100)**2


if IMC < 18.5:
 print(f'seu IMC: {IMC} é de frango, vai treinar')

elif IMC >= 18.5 and IMC < 24.9:
 print(f'seu IMC: {IMC} é de ser humano normal parabens')

elif IMC >= 24.9 and IMC < 29.9:
 print(f'seu IMC: {IMC} é de ser humano que come um pouco mais que o normal parabens')

elif IMC >= 30 and IMC 190< 39.9:
 print(f'seu IMC: {IMC} é de estágio inicial de obesidade, procure emagrecer')

else: 
 print(f'seu IMC: {IMC} é de obesidade grave, procure emagrecer urgentemente')



#stepple fera CC ou SI 2k24



