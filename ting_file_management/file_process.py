import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for process in instance._data:
        if path_file in process["nome_do_arquivo"]:
            return path_file
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }
    instance.enqueue(data)

    print(data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    if not len(instance):
        print("Não há elementos")
    else:
        removed_data = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {removed_data} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
