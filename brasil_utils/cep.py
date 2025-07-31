"""
Módulo para consulta de CEP via API do ViaCEP.
"""

import requests
import re


def limpar_cep(cep):
    """
    Remove caracteres especiais de um CEP.
    
    Args:
        cep (str): CEP a ser limpo
        
    Returns:
        str: CEP apenas com números
    """
    return re.sub(r'\D', '', str(cep))


def validar_cep(cep):
    """
    Valida se um CEP tem o formato correto.
    
    Args:
        cep (str): CEP a ser validado
        
    Returns:
        bool: True se o CEP for válido, False caso contrário
    """
    cep_limpo = limpar_cep(cep)
    return len(cep_limpo) == 8 and cep_limpo.isdigit()


def buscar_cep(cep):
    """
    Busca informações de endereço através do CEP usando a API do ViaCEP.
    
    Args:
        cep (str): CEP a ser consultado
        
    Returns:
        dict: Dicionário com informações do endereço ou None se não encontrado
    """
    if not validar_cep(cep):
        return {"erro": "CEP inválido"}
    
    cep_limpo = limpar_cep(cep)
    
    try:
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        dados = response.json()
        
        if "erro" in dados:
            return {"erro": "CEP não encontrado"}
        
        return {
            "cep": dados.get("cep", ""),
            "logradouro": dados.get("logradouro", ""),
            "complemento": dados.get("complemento", ""),
            "bairro": dados.get("bairro", ""),
            "localidade": dados.get("localidade", ""),
            "uf": dados.get("uf", ""),
            "ibge": dados.get("ibge", ""),
            "gia": dados.get("gia", ""),
            "ddd": dados.get("ddd", ""),
            "siafi": dados.get("siafi", "")
        }
        
    except requests.exceptions.RequestException as e:
        return {"erro": f"Erro na consulta: {str(e)}"}
    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}


def formatar_cep(cep):
    """
    Formata um CEP com hífen.
    
    Args:
        cep (str): CEP a ser formatado
        
    Returns:
        str: CEP formatado ou string vazia se inválido
    """
    if not validar_cep(cep):
        return ""
    
    cep_limpo = limpar_cep(cep)
    return f"{cep_limpo[:5]}-{cep_limpo[5:]}"
