import nltk as nltk

with open("files/artigos.txt", "r", encoding="utf8") as f:
    artigos = f.read()
print(artigos[:500])


texto_exemplo = "Olá, tudo bem?"
palavras_separadas = texto_exemplo.split()


print(palavras_separadas)
print(len(palavras_separadas))

texto_exemplo = "Olá, tudo bem?"
tokens = texto_exemplo.split()
print(len(tokens))
print(tokens)

nltk.download('punkt')
palavras_separadas = nltk.tokenize.word_tokenize(texto_exemplo)
print(palavras_separadas)



def separa_palavras(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)
    return lista_palavras


print(separa_palavras(palavras_separadas))


lista_tokens = nltk.tokenize.word_tokenize(artigos)
lista_palavras = separa_palavras(lista_tokens)
print(f"O número de palavras é: {len(lista_palavras)}")

print(lista_palavras[:5])


def normalizacao(lista_palavras):
    lista_normalizada = []
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada

lista_normalizada = normalizacao(lista_palavras)
print(lista_normalizada[:5])


len(set(lista_normalizada))


lista = "lgica"
(lista[:1], lista[1:])
palavra_exemplo = 'lgica'





palavra_exemplo = "lgica"

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras


def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    return palavras_geradas

palavras_geradas = gerador_palavras(palavra_exemplo)
print(palavras_geradas)


