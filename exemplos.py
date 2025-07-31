"""
Exemplos de uso do pacote brasil_utils
"""

from brasil_utils import validadores, cep, formatadores

def exemplos_validadores():
    """Exemplos de validação de documentos brasileiros"""
    print("=== VALIDAÇÃO DE DOCUMENTOS ===")
    
    # Exemplos de CPF
    cpfs_teste = ["123.456.789-09", "11111111111", "123.456.789-10"]
    
    for cpf in cpfs_teste:
        valido = validadores.validar_cpf(cpf)
        formatado = validadores.formatar_cpf(cpf)
        print(f"CPF: {cpf} - Válido: {valido} - Formatado: {formatado}")
    
    print()
    
    # Exemplos de CNPJ
    cnpjs_teste = ["11.222.333/0001-81", "11222333000181", "00.000.000/0000-00"]
    
    for cnpj in cnpjs_teste:
        valido = validadores.validar_cnpj(cnpj)
        formatado = validadores.formatar_cnpj(cnpj)
        print(f"CNPJ: {cnpj} - Válido: {valido} - Formatado: {formatado}")


def exemplos_cep():
    """Exemplos de consulta de CEP"""
    print("\n=== CONSULTA DE CEP ===")
    
    ceps_teste = ["01310-100", "20040020", "00000-000"]
    
    for cep_teste in ceps_teste:
        print(f"\nConsultando CEP: {cep_teste}")
        resultado = cep.buscar_cep(cep_teste)
        
        if "erro" in resultado:
            print(f"Erro: {resultado['erro']}")
        else:
            print(f"Endereço: {resultado['logradouro']}")
            print(f"Bairro: {resultado['bairro']}")
            print(f"Cidade: {resultado['localidade']}/{resultado['uf']}")


def exemplos_formatadores():
    """Exemplos de formatação de valores brasileiros"""
    print("\n=== FORMATAÇÃO DE VALORES ===")
    
    # Formatação de moeda
    valores = [1234.56, 999.99, 0.50]
    for valor in valores:
        formatado = formatadores.formatar_real(valor)
        print(f"Valor: {valor} -> {formatado}")
    
    print()
    
    # Formatação de telefone
    telefones = ["11999887766", "1133334444", "5511999887766"]
    for telefone in telefones:
        formatado = formatadores.formatar_telefone(telefone)
        print(f"Telefone: {telefone} -> {formatado}")
    
    print()
    
    # Formatação de porcentagem
    percentuais = [0.15, 0.0525, 1.2]
    for perc in percentuais:
        formatado = formatadores.formatar_porcentagem(perc)
        print(f"Percentual: {perc} -> {formatado}")


def exemplos_feriados():
    """Exemplos de cálculo de feriados (requer python-dateutil)"""
    print("\n=== FERIADOS NACIONAIS ===")
    
    try:
        from brasil_utils import feriados
        from datetime import date
        
        ano_atual = date.today().year
        todos_feriados_ano = feriados.todos_feriados(ano_atual)
        
        print(f"Feriados nacionais de {ano_atual}:")
        for nome, data_feriado in sorted(todos_feriados_ano.items(), key=lambda x: x[1]):
            print(f"- {nome}: {data_feriado.strftime('%d/%m/%Y')}")
        
        # Verifica se hoje é feriado
        hoje = date.today()
        if feriados.eh_feriado(hoje):
            print(f"\nHoje ({hoje.strftime('%d/%m/%Y')}) é feriado!")
        else:
            print(f"\nHoje ({hoje.strftime('%d/%m/%Y')}) não é feriado.")
        
        # Próximo feriado
        proximo = feriados.proximo_feriado()
        if proximo:
            nome_feriado, data_feriado = proximo
            print(f"Próximo feriado: {nome_feriado} em {data_feriado.strftime('%d/%m/%Y')}")
    
    except ImportError:
        print("Módulo de feriados não disponível. Instale python-dateutil com:")
        print("pip install python-dateutil")


if __name__ == "__main__":
    exemplos_validadores()
    exemplos_cep()
    exemplos_formatadores()
    exemplos_feriados()
