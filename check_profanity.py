import urllib.request as request
import urllib.parse as parse


def read_text():
    teste = open(
        r'C:\Users\Usuario\Documents\Rafael\Cursos\Programação\Python\Udacity\FundamentosProgramacaoPython\teste.txt')
    conteudo_arquivo = teste.read()
    teste.close()
    check_profanity(conteudo_arquivo)


def check_profanity(text_to_check):
    url = 'http://www.wdylike.appspot.com/?q='
    q = parse.quote(text_to_check)
    connection = request.urlopen(url + q)
    output = connection.read()
    print(output)
    connection.close()
    # if 'false' in output:
    # print('Arquvio liberado, não contêm palavrões...')
    # elif 'true' in output:
    # print('Cuidado, arquivo contêm palavrões...')
    # else:
    # print('Arquivo não pode ser lido...')


read_text()
