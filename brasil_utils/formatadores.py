"""
Módulo para formatação de valores brasileiros (moeda, telefone, etc).
"""

import locale
from datetime import datetime, date
import re


def formatar_real(valor, simbolo=True):
    """
    Formata um valor numérico como moeda brasileira (Real).
    
    Args:
        valor (float): Valor a ser formatado
        simbolo (bool): Se deve incluir o símbolo R$
        
    Returns:
        str: Valor formatado como moeda brasileira
    """
    try:
        # Tenta usar a localização brasileira
        try:
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        except locale.Error:
            # Fallback para formatação manual
            pass
        
        valor_formatado = f"{valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        
        if simbolo:
            return f"R$ {valor_formatado}"
        return valor_formatado
        
    except Exception:
        return str(valor)


def formatar_telefone(telefone):
    """
    Formata um número de telefone brasileiro.
    
    Args:
        telefone (str): Telefone a ser formatado
        
    Returns:
        str: Telefone formatado ou string original se inválido
    """
    # Remove caracteres não numéricos
    numeros = re.sub(r'\D', '', telefone)
    
    # Telefone com código do país (13 dígitos: +55 11 99999-9999)
    if len(numeros) == 13 and numeros.startswith('55'):
        return f"+{numeros[:2]} ({numeros[2:4]}) {numeros[4:9]}-{numeros[9:]}"
    
    # Telefone com DDD e celular (11 dígitos: 11 99999-9999)
    elif len(numeros) == 11:
        return f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"
    
    # Telefone com DDD e fixo (10 dígitos: 11 9999-9999)
    elif len(numeros) == 10:
        return f"({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}"
    
    # Telefone sem DDD e celular (9 dígitos: 99999-9999)
    elif len(numeros) == 9:
        return f"{numeros[:5]}-{numeros[5:]}"
    
    # Telefone sem DDD e fixo (8 dígitos: 9999-9999)
    elif len(numeros) == 8:
        return f"{numeros[:4]}-{numeros[4:]}"
    
    # Retorna original se não conseguir formatar
    return telefone


def formatar_data_brasileira(data, formato="%d/%m/%Y"):
    """
    Formata uma data no padrão brasileiro.
    
    Args:
        data (datetime/date/str): Data a ser formatada
        formato (str): Formato de saída
        
    Returns:
        str: Data formatada
    """
    try:
        if isinstance(data, str):
            # Tenta diferentes formatos de entrada
            formatos_entrada = [
                "%Y-%m-%d",
                "%d/%m/%Y",
                "%d-%m-%Y",
                "%Y/%m/%d"
            ]
            
            for fmt in formatos_entrada:
                try:
                    data = datetime.strptime(data, fmt).date()
                    break
                except ValueError:
                    continue
        
        if isinstance(data, datetime):
            data = data.date()
        
        if isinstance(data, date):
            return data.strftime(formato)
        
        return str(data)
        
    except Exception:
        return str(data)


def formatar_porcentagem(valor, casas_decimais=2):
    """
    Formata um valor como porcentagem brasileira.
    
    Args:
        valor (float): Valor a ser formatado (0.15 = 15%)
        casas_decimais (int): Número de casas decimais
        
    Returns:
        str: Valor formatado como porcentagem
    """
    try:
        percentual = valor * 100
        if casas_decimais == 0:
            return f"{percentual:.0f}%"
        else:
            formatado = f"{percentual:.{casas_decimais}f}%"
            return formatado.replace('.', ',')
    except Exception:
        return str(valor)


def remover_acentos(texto):
    """
    Remove acentos de um texto.
    
    Args:
        texto (str): Texto a ser processado
        
    Returns:
        str: Texto sem acentos
    """
    acentos = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c', 'ñ': 'n',
        'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
        'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
        'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
        'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
        'Ç': 'C', 'Ñ': 'N'
    }
    
    resultado = texto
    for acento, sem_acento in acentos.items():
        resultado = resultado.replace(acento, sem_acento)
    
    return resultado
