
from faker import Faker
import random
import string
from listaValoresPreenchimento import *
from connectionMongo import *
from connectionPostgres import *

locales = 'pt-BR'
fake = Faker(locales)

listaAtributos, listaGrupos, listaCodigoTributacao = connectionPostgres(40180)

def generate_codigoProduto():
    return fake.pyint()


def generate_nomeProduto():
    return fake.pystr()


def generate_codigoBarras():
    return fake.ean()


def generate_precoVenda():
    return round(random.uniform(0.00, 1000.00), 2)


def generate_marca():
    return ''.join(random.choices(string.ascii_uppercase, k=5))


def generate_peso():
    return round(random.uniform(0.00, 90.00), 3)


def generate_unidadeMedida():
    return random.choice(unidadeMedida)


def generate_valorAtributo():
    return ''.join(random.choices(string.ascii_uppercase, k=2))


def generate_informacoesAdicionais():
    return fake.catch_phrase()


def generate_estoqueMinimo():
    return '1'


def generate_estoque():
    return fake.pyint()


def generate_origem():
    return random.choice(origem)


def generate_tipoProduto():
    return random.choice(tipoProduto)


def generate_NCM():
    return random.choice(ncm)


def generate_exTipi():
    return fake.pyint()


def generate_controleFCI():
    return random.getrandbits(105)


def generate_aliquotaTributosFederal():
    return fake.pyint()


def generate_aliquotaTributosEstadual():
    return fake.pyint()


def generate_CEST():
    return random.choice(cest)


def generate_codigoTributacao():
    return random.choice(listaCodigoTributacao)


def generate_codigoBeneficioUF():
    return random.getrandbits(25)


def generate_fornecedor():
    return generateDocumentoFornecedor()


def generateDocumentoFornecedor():
    return random.choice(documentosFornecedor)


def listDocumentDataBase():
    return listaDocumentos


def generate_atributo():
    return random.choice(listaAtributos)


def generate_grupo():
    return random.choice(listaGrupos)
