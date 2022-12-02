def exists_word(word, instance):
    """Aqui irá sua implementação"""
    list_text = []
    occurrences = []
    for index, line in enumerate(instance._data[0]["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            occurrences.append({"linha": index + 1})
    for index, line in enumerate(instance._data[0]["linhas_do_arquivo"]):
        if word.lower() not in line.lower():
            return list_text
        else:
            data = {
                "palavra": word,
                "arquivo": instance._data[0]["nome_do_arquivo"],
                "ocorrencias": occurrences,
            }
            list_text.append(data)
            return list_text


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    list_text = []
    occurrences = []

    for index, line in enumerate(instance._data[0]["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            occurrences.append({"linha": index + 1, "conteudo": line})

    if 0 < len(occurrences):
        list_text.append(
            {
                "palavra": word,
                "arquivo": instance._data[0]["nome_do_arquivo"],
                "ocorrencias": occurrences,
            }
        )

    return list_text
