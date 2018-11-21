import os


def rename_files():
    # listar os arquivos dentro da pasta
    file_list = os.listdir(
        r"C:\Users\Usuario\Documents\Rafael\Cursos\Programação\Python\Udacity\FundamentosProgramacaoPython\prank")
    # mostra o diretório atual
    saved_path = os.getcwd()
    print("Current Working Directory is" + saved_path)
    # muda o diretório atual
    os.chdir(r"C:\Users\Usuario\Documents\Rafael\Cursos\Programação\Python\Udacity\FundamentosProgramacaoPython\prank")
    saved_path = os.getcwd()
    print("Current Working Directory is" + saved_path)
    # renomear os arquivos
    for file_name in file_list:
        print("Old name - " + file_name)
        print("New Name - " + file_name.strip("0123456789"))
        os.rename(file_name, file_name.strip("0123456789"))
        # renomeia cada arquivo, retirando os números deles
    os.chdir(saved_path)


rename_files()
