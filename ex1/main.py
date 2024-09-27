
def aumenta_salario(departamento, percentual): # supondo que o percentual seja decimal
    import json # caso já não tenha importado
    with open('ex1/funcionarios.json','r',encoding='-8') as file:
        fr = file.read()
        funcionarios = json.loads(fr)
    
    for funcionario in funcionarios:
        if funcionario["departamento"] == departamento:
            funcionario['salario'] *= (1 + float(percentual))

    with open('ex1/funcionarios.json','w',encoding='UTF-8') as file:
        json.dump([funcionarios], file, indent=4)

aumenta_salario('RH','0.5')