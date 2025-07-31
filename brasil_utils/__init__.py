"""
brasil_utils - Utilitários Python para desenvolvedores brasileiros

Este pacote oferece funcionalidades essenciais para aplicações brasileiras:
- Validação de CPF e CNPJ
- Consulta de CEP
- Formatação de moeda brasileira
- Cálculo de feriados nacionais
- Formatação de telefones
"""

__version__ = "0.0.1"
__author__ = "Samuel Lucas"

# Importações principais para facilitar o uso
from .validadores import validar_cpf, validar_cnpj, formatar_cpf, formatar_cnpj
from .formatadores import formatar_real, formatar_telefone, formatar_data_brasileira
from .cep import buscar_cep, validar_cep, formatar_cep

# Importações condicionais (dependem de bibliotecas externas)
try:
    from .feriados import todos_feriados, eh_feriado, proximo_feriado
except ImportError:
    # Se dateutil não estiver instalado, as funções de feriados não estarão disponíveis
    pass

__all__ = [
    'validar_cpf',
    'validar_cnpj', 
    'formatar_cpf',
    'formatar_cnpj',
    'buscar_cep',
    'validar_cep',
    'formatar_cep',
    'formatar_real',
    'formatar_telefone',
    'formatar_data_brasileira',
    'todos_feriados',
    'eh_feriado',
    'proximo_feriado'
]