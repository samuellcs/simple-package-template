"""
Módulo para validação de documentos brasileiros (CPF, CNPJ).
"""

import re


def limpar_documento(documento):
    """
    Remove caracteres especiais de um documento.
    
    Args:
        documento (str): Documento a ser limpo
        
    Returns:
        str: Documento apenas com números
    """
    return re.sub(r'\D', '', str(documento))


def validar_cpf(cpf):
    """
    Valida um número de CPF brasileiro.
    
    Args:
        cpf (str): CPF a ser validado
        
    Returns:
        bool: True se o CPF for válido, False caso contrário
    """
    cpf = limpar_documento(cpf)
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = 11 - (soma % 11)
    if primeiro_digito >= 10:
        primeiro_digito = 0
    
    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = 11 - (soma % 11)
    if segundo_digito >= 10:
        segundo_digito = 0
    
    # Verifica se os dígitos calculados conferem
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"


def validar_cnpj(cnpj):
    """
    Valida um número de CNPJ brasileiro.
    
    Args:
        cnpj (str): CNPJ a ser validado
        
    Returns:
        bool: True se o CNPJ for válido, False caso contrário
    """
    cnpj = limpar_documento(cnpj)
    
    # Verifica se tem 14 dígitos
    if len(cnpj) != 14:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cnpj == cnpj[0] * 14:
        return False
    
    # Sequência de pesos para os cálculos
    pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    
    # Calcula o primeiro dígito verificador
    soma = sum(int(cnpj[i]) * pesos[i] for i in range(12))
    primeiro_digito = 11 - (soma % 11)
    if primeiro_digito >= 10:
        primeiro_digito = 0
    
    # Calcula o segundo dígito verificador
    pesos.insert(0, 6)
    soma = sum(int(cnpj[i]) * pesos[i] for i in range(13))
    segundo_digito = 11 - (soma % 11)
    if segundo_digito >= 10:
        segundo_digito = 0
    
    # Verifica se os dígitos calculados conferem
    return cnpj[-2:] == f"{primeiro_digito}{segundo_digito}"


def formatar_cpf(cpf):
    """
    Formata um CPF com pontos e hífen.
    
    Args:
        cpf (str): CPF a ser formatado
        
    Returns:
        str: CPF formatado ou string vazia se inválido
    """
    cpf = limpar_documento(cpf)
    if validar_cpf(cpf):
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return ""


def formatar_cnpj(cnpj):
    """
    Formata um CNPJ com pontos, barra e hífen.
    
    Args:
        cnpj (str): CNPJ a ser formatado
        
    Returns:
        str: CNPJ formatado ou string vazia se inválido
    """
    cnpj = limpar_documento(cnpj)
    if validar_cnpj(cnpj):
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
    return ""
