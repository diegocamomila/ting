1 - Crie o ambiente virtual para o projeto
python3 -m venv .venv && source .venv/bin/activate
2 - Instale as dependências
python3 -m pip install -r dev-requirements.txt
3 - Para garantir a qualidade do código, vamos utilizar neste projeto o linter Flake8
$ python3 -m flake8

Ambiente Virtual
1 - criar o ambiente virtual
$ python3 -m venv .venv
2 - ativar o ambiente virtual
$ source .venv/bin/activate
3 - instalar as dependências no ambiente virtual
$ python3 -m pip install -r dev-requirements.txt

Executar os Testes
1 - todos testes
$ python3 -m pytest
2 - Caso precise executar apenas uma função de testes basta executar o comando:
$ python3 -m pytest -k nome_da_func_de_tests
3 - Para executar um teste específico de um arquivo, basta executar o comando:
$ python -m pytest -x tests/nome_do_arquivo.py::test_nome_do_teste

1 - A len()função retorna o número de itens em um objeto
https://www.w3schools.com/python/ref_func_len.asp
https://blog.betrybe.com/python/len-python/

O append()método acrescenta um elemento ao final da lista.
https://www.w3schools.com/python/ref_list_append.asp
https://www.programiz.com/python-programming/methods/list/append

O pop()método remove o elemento na posição especificada.
https://www.w3schools.com/python/ref_list_pop.asp
https://www.simplilearn.com/tutorials/python-tutorial/pop-in-python

2 - not in - você pode verificar se um valor não está em uma coleção com a operação
https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files
https://www.codingem.com/in-operator-in-python/

Use a open()função com o 'r'modo para abrir um arquivo de texto para leitura.
Use o método read(), readline()ou readlines()para ler um arquivo de texto.
https://www.pythontutorial.net/python-basics/python-read-text-file

O split()método divide uma string em uma lista.
Você pode especificar o separador, o separador padrão é qualquer espaço em branco. No exercicio pede para usar como separador "\n"
https://www.w3schools.com/python/ref_string_split.asp
