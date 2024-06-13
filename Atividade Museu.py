class ObraDeArte:
    def __init__(self, titulo, data_criacao, tema, estilo, descricao, tecnica, autor, localizacao):
        self.titulo = titulo
        self.data_criacao = data_criacao
        self.tema = tema
        self.estilo = estilo
        self.descricao = descricao
        self.tecnica = tecnica
        self.autor = autor
        self.localizacao = localizacao
        self.documentos_relacionados = []
        self.pesquisas_sobre_figuras = []

    def adicionar_documento(self, documento):
        self.documentos_relacionados.append(documento)

    def adicionar_pesquisa(self, pesquisa):
        self.pesquisas_sobre_figuras.append(pesquisa)

class Artista:
    def __init__(self, nome, data_nascimento, local_nascimento, biografia, estilos_associados):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.local_nascimento = local_nascimento
        self.biografia = biografia
        self.estilos_associados = estilos_associados

class EstiloArtistico:
    def __init__(self, denominacao, periodo_influencia, descricao_caracteristicas, escola_representativa):
        self.denominacao = denominacao
        self.periodo_influencia = periodo_influencia
        self.descricao_caracteristicas = descricao_caracteristicas
        self.escola_representativa = escola_representativa

class Emprestimo:
    def __init__(self, obra, periodo, evento, responsavel, tema):
        self.obra = obra
        self.periodo = periodo
        self.evento = evento
        self.responsavel = responsavel
        self.tema = tema

class VisitaGuiada:
    def __init__(self, tema, descricao, obras):
        self.tema = tema
        self.descricao = descricao
        self.obras = obras

def salvar_dados(objeto, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for key, value in objeto.__dict__.items():
                arquivo.write(f'{key}: {value}\n')
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def ler_dados(nome_arquivo):
    dados = {}
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                key, value = linha.strip().split(': ')
                dados[key] = value
    except Exception as e:
        print(f"Erro ao ler dados: {e}")
    return dados

def ordenar_obras_por_titulo(obras):
    for i in range(len(obras)):
        min_idx = i
        for j in range(i+1, len(obras)):
            if obras[min_idx].titulo > obras[j].titulo:
                min_idx = j
        obras[i], obras[min_idx] = obras[min_idx], obras[i]

if __name__ == "__main__":
    obra1 = ObraDeArte("Mona Lisa", "1503", "Retrato", "Renascentista", "Descrição da Mona Lisa", "Óleo sobre tela", "Leonardo da Vinci", "Sala 1")
    obra2 = ObraDeArte("O Grito", "1893", "Expressão", "Expressionismo", "Descrição de O Grito", "Óleo, têmpera e pastel sobre papelão", "Edvard Munch", "Sala 2")

    artista1 = Artista("Leonardo da Vinci", "1452-04-15", "Vinci, Itália", "Biografia de Leonardo", ["Renascentista"])
    artista2 = Artista("Edvard Munch", "1863-12-12", "Loten, Noruega", "Biografia de Munch", ["Expressionismo"])

    salvar_dados(obra1, "obra1.txt")
    salvar_dados(artista1, "artista1.txt")

    dados_obra1 = ler_dados("obra1.txt")
    dados_artista1 = ler_dados("artista1.txt")

    print(dados_obra1)
    print(dados_artista1)

    obras = [obra1, obra2]
    ordenar_obras_por_titulo(obras)
    for obra in obras:
        print(obra.titulo)
