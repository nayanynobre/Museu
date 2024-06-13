import json
from typing import List

class Obra:
    def __init__(self, titulo, data_criacao, tema, estilo_artistico, descricao, tecnica, autor, localizacao):
        self.titulo = titulo
        self.data_criacao = data_criacao
        self.tema = tema
        self.estilo_artistico = estilo_artistico
        self.descricao = descricao
        self.tecnica = tecnica
        self.autor = autor
        self.localizacao = localizacao
        self.documentos = []
        self.pessoa_retratada = None

    def adicionar_documento(self, documento):
        self.documentos.append(documento)

    def definir_pessoa_retratada(self, pessoa):
        self.pessoa_retratada = pessoa

class Artista:
    def __init__(self, nome, data_nascimento, local_nascimento, biografia, estilos_artistico):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.local_nascimento = local_nascimento
        self.biografia = biografia
        self.estilos_artistico = estilos_artistico

class EstiloArtistico:
    def __init__(self, denominacao, periodo_influencia, descricao, escola_representativa):
        self.denominacao = denominacao
        self.periodo_influencia = periodo_influencia
        self.descricao = descricao
        self.escola_representativa = escola_representativa

class Documento:
    def __init__(self, tipo, descricao):
        self.tipo = tipo
        self.descricao = descricao

class PessoaRetratada:
    def __init__(self, nome, biografia):
        self.nome = nome
        self.biografia = biografia

class Emprestimo:
    def __init__(self, periodo, evento, responsavel, tema):
        self.periodo = periodo
        self.evento = evento
        self.responsavel = responsavel
        self.tema = tema

class Roteiro:
    def __init__(self, tema, descricao, obras):
        self.tema = tema
        self.descricao = descricao
        self.obras = obras

def quicksort(lista, key=lambda x: x):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    menores = [x for x in lista[1:] if key(x) <= key(pivot)]
    maiores = [x for x in lista[1:] if key(x) > key(pivot)]
    return quicksort(menores, key) + [pivot] + quicksort(maiores, key)

def salvar_dados(filename, dados):
    try:
        with open(filename, 'w') as file:
            json.dump(dados, file, indent=4, default=lambda o: o.__dict__)
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def carregar_dados(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return []

if __name__ == "__main__":
    estilo1 = EstiloArtistico("Impressionismo", "1860-1900", "Caracteriza-se por pinceladas visíveis, ênfase na luz...", "Escola de Paris")
    artista1 = Artista("Claude Monet", "1840-11-14", "Paris, França", "Pintor francês, um dos fundadores do Impressionismo...", [estilo1])
    
    obra1 = Obra("Impressão, nascer do sol", "1872", "Paisagem", estilo1, "Uma das obras mais famosas de Monet...", "Óleo sobre tela", artista1, "Sala 1")
    documento1 = Documento("Carta", "Carta de Monet sobre a obra")
    obra1.adicionar_documento(documento1)
    
    pessoa1 = PessoaRetratada("Nobre XYZ", "Biografia do nobre XYZ")
    obra1.definir_pessoa_retratada(pessoa1)

    obras = [obra1]
    artistas = [artista1]
    estilos = [estilo1]

    salvar_dados('obras.json', obras)
    salvar_dados('artistas.json', artistas)
    salvar_dados('estilos.json', estilos)

    obras_carregadas = carregar_dados('obras.json')
    artistas_carregados = carregar_dados('artistas.json')
    estilos_carregados = carregar_dados('estilos.json')

    print(obras_carregadas)
    print(artistas_carregados)
    print(estilos_carregados)

    obras_ordenadas = quicksort(obras, key=lambda x: x.titulo)
    for obra in obras_ordenadas:
        print(obra.titulo)