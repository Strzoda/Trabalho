valor = int(input('Quanto voce ganha por hora: '))
horas = int(input('Numero de horas trabalhadas no mes: '))
salario = valor * horas
ir = (11/100.0 * salario)
print ('Imposto de renda: ',ir)
inss = (8/100.0 * salario)
print ('INSS: ',inss)
sind = (5/100.0 * salario)
print ('Sindicato: ',sind)
desc = ir + inss + sind
salarioL = salario - desc
print ('O desconto total do salario bruto(',salario,'R$)',
       'foi',desc,'\nO salario liquido ficou,',salarioL)