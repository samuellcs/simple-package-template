"""
Módulo para cálculo de feriados nacionais brasileiros.
"""

from datetime import datetime, date, timedelta
from dateutil.easter import easter


def feriados_fixos(ano):
    """
    Retorna os feriados fixos do Brasil para um determinado ano.
    
    Args:
        ano (int): Ano para calcular os feriados
        
    Returns:
        dict: Dicionário com os feriados fixos
    """
    return {
        'Ano Novo': date(ano, 1, 1),
        'Tiradentes': date(ano, 4, 21),
        'Dia do Trabalhador': date(ano, 5, 1),
        'Independência do Brasil': date(ano, 9, 7),
        'Nossa Senhora Aparecida': date(ano, 10, 12),
        'Finados': date(ano, 11, 2),
        'Proclamação da República': date(ano, 11, 15),
        'Natal': date(ano, 12, 25)
    }


def feriados_moveis(ano):
    """
    Retorna os feriados móveis do Brasil para um determinado ano.
    
    Args:
        ano (int): Ano para calcular os feriados
        
    Returns:
        dict: Dicionário com os feriados móveis
    """
    pascoa = easter(ano)
    
    return {
        'Carnaval': pascoa - timedelta(days=47),  # Segunda-feira de carnaval
        'Sexta-feira Santa': pascoa - timedelta(days=2),
        'Corpus Christi': pascoa + timedelta(days=60)
    }


def todos_feriados(ano):
    """
    Retorna todos os feriados nacionais brasileiros para um determinado ano.
    
    Args:
        ano (int): Ano para calcular os feriados
        
    Returns:
        dict: Dicionário com todos os feriados
    """
    feriados = {}
    feriados.update(feriados_fixos(ano))
    feriados.update(feriados_moveis(ano))
    
    return feriados


def eh_feriado(data_verificar):
    """
    Verifica se uma data é feriado nacional no Brasil.
    
    Args:
        data_verificar (date/datetime/str): Data a ser verificada
        
    Returns:
        bool: True se for feriado, False caso contrário
    """
    # Converte string para date se necessário
    if isinstance(data_verificar, str):
        try:
            data_verificar = datetime.strptime(data_verificar, '%Y-%m-%d').date()
        except ValueError:
            try:
                data_verificar = datetime.strptime(data_verificar, '%d/%m/%Y').date()
            except ValueError:
                return False
    
    # Converte datetime para date se necessário
    if isinstance(data_verificar, datetime):
        data_verificar = data_verificar.date()
    
    ano = data_verificar.year
    feriados = todos_feriados(ano)
    
    return data_verificar in feriados.values()


def proximo_feriado(data_referencia=None):
    """
    Retorna o próximo feriado nacional a partir de uma data de referência.
    
    Args:
        data_referencia (date/datetime): Data de referência (padrão: hoje)
        
    Returns:
        tuple: (nome_feriado, data_feriado) ou None se não houver
    """
    if data_referencia is None:
        data_referencia = date.today()
    
    if isinstance(data_referencia, datetime):
        data_referencia = data_referencia.date()
    
    # Verifica feriados do ano atual
    ano_atual = data_referencia.year
    feriados_ano = todos_feriados(ano_atual)
    
    # Filtra feriados futuros
    feriados_futuros = {
        nome: data_feriado for nome, data_feriado in feriados_ano.items()
        if data_feriado > data_referencia
    }
    
    # Se não há feriados futuros no ano atual, verifica o próximo ano
    if not feriados_futuros:
        feriados_proximo_ano = todos_feriados(ano_atual + 1)
        feriados_futuros = feriados_proximo_ano
    
    if feriados_futuros:
        # Encontra o feriado mais próximo
        proximo = min(feriados_futuros.items(), key=lambda x: x[1])
        return proximo
    
    return None


def dias_uteis_entre(data_inicio, data_fim, incluir_feriados=False):
    """
    Calcula o número de dias úteis entre duas datas.
    
    Args:
        data_inicio (date/datetime): Data de início
        data_fim (date/datetime): Data de fim
        incluir_feriados (bool): Se feriados devem ser considerados dias úteis
        
    Returns:
        int: Número de dias úteis
    """
    if isinstance(data_inicio, datetime):
        data_inicio = data_inicio.date()
    if isinstance(data_fim, datetime):
        data_fim = data_fim.date()
    
    if data_inicio > data_fim:
        data_inicio, data_fim = data_fim, data_inicio
    
    dias_uteis = 0
    data_atual = data_inicio
    
    while data_atual <= data_fim:
        # Segunda a sexta (0-4) são dias úteis
        if data_atual.weekday() < 5:
            # Se não incluir feriados, verifica se não é feriado
            if incluir_feriados or not eh_feriado(data_atual):
                dias_uteis += 1
        
        data_atual += timedelta(days=1)
    
    return dias_uteis


def feriados_por_mes(ano, mes):
    """
    Retorna os feriados de um mês específico.
    
    Args:
        ano (int): Ano
        mes (int): Mês (1-12)
        
    Returns:
        dict: Feriados do mês especificado
    """
    todos_feriados_ano = todos_feriados(ano)
    
    feriados_mes = {
        nome: data_feriado for nome, data_feriado in todos_feriados_ano.items()
        if data_feriado.month == mes
    }
    
    return feriados_mes
