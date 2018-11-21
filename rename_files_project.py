import os
from time import sleep


def rename_files():
    file_list = os.listdir(
        r"C:\Users\Usuario\Documents\Rafael\Cursos\Programação\Python\Udacity\FundamentosProgramacaoPython\mensagem")
    os.chdir(
        r"C:\Users\Usuario\Documents\Rafael\Cursos\Programação\Python\Udacity\FundamentosProgramacaoPython\mensagem")
    for file_name in file_list:
        print("Nome antigo: " + file_name)
        print("Novo nome: " + file_name.strip("0123456789"))
        os.rename(file_name, file_name.strip("0123456789"))
        sleep(0.4)


rename_files()
