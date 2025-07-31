# 🇧🇷 Brasil Utils

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/brasil-utils-samuellcs.svg)](https://badge.fury.io/py/brasil-utils-samuellcs)

**Brasil Utils** é uma biblioteca Python que oferece utilitários essenciais para desenvolvedores que trabalham com dados brasileiros. Simplifique tarefas comuns como validação de documentos, consulta de CEP, formatação de valores monetários e muito mais!

## 🚀 Funcionalidades

- ✅ **Validação de Documentos**: CPF e CNPJ
- 📍 **Consulta de CEP**: Integração com API ViaCEP
- 💰 **Formatação Monetária**: Real brasileiro (R$)
- 📱 **Formatação de Telefone**: Números brasileiros
- 📅 **Cálculo de Feriados**: Feriados nacionais brasileiros
- 🎯 **Formatação de Dados**: Datas, porcentagens e mais

## 📦 Instalação

### Via pip (recomendado)

```bash
pip install brasil-utils-samuellcs
```

### Instalação local para desenvolvimento

```bash
git clone https://github.com/samuellcs/simple-package-template.git
cd simple-package-template
pip install -e .
```

## 🔧 Uso Rápido

### Validação de Documentos

```python
from brasil_utils import validar_cpf, validar_cnpj, formatar_cpf, formatar_cnpj

# Validação de CPF
cpf_valido = validar_cpf("123.456.789-09")  # True ou False
cpf_formatado = formatar_cpf("12345678909")  # "123.456.789-09"

# Validação de CNPJ
cnpj_valido = validar_cnpj("11.222.333/0001-81")  # True ou False
cnpj_formatado = formatar_cnpj("11222333000181")  # "11.222.333/0001-81"
```

### Consulta de CEP

```python
from brasil_utils import buscar_cep, validar_cep, formatar_cep

# Buscar informações do CEP
endereco = buscar_cep("01310-100")
print(endereco)
# {
#   "cep": "01310-100",
#   "logradouro": "Avenida Paulista",
#   "bairro": "Bela Vista",
#   "localidade": "São Paulo",
#   "uf": "SP"
# }

# Validar formato do CEP
cep_valido = validar_cep("01310-100")  # True
cep_formatado = formatar_cep("01310100")  # "01310-100"
```

### Formatação de Valores

```python
from brasil_utils import formatar_real, formatar_telefone, formatar_data_brasileira

# Formatação monetária
valor_formatado = formatar_real(1234.56)  # "R$ 1.234,56"

# Formatação de telefone
telefone_formatado = formatar_telefone("11999887766")  # "(11) 99988-7766"

# Formatação de data
from datetime import date
data_formatada = formatar_data_brasileira(date(2024, 12, 25))  # "25/12/2024"
```

### Feriados Nacionais

```python
from brasil_utils import todos_feriados, eh_feriado, proximo_feriado
from datetime import date

# Obter todos os feriados do ano
feriados_2024 = todos_feriados(2024)
print(feriados_2024)

# Verificar se uma data é feriado
natal = date(2024, 12, 25)
if eh_feriado(natal):
    print("É feriado!")

# Próximo feriado
nome, data = proximo_feriado()
print(f"Próximo feriado: {nome} em {data}")
```

## 📚 Exemplos Completos

Execute o arquivo de exemplos para ver todas as funcionalidades:

```bash
python exemplos.py
```

## 🛠️ Dependências

### Obrigatórias
- Python 3.8+
- requests >= 2.25.0

### Opcionais
- python-dateutil >= 2.8.0 (para funcionalidades de feriados)

Para instalar com todas as dependências:

```bash
pip install brasil-utils-samuellcs[complete]
```

## 🔍 API Reference

### Módulo `validadores`

| Função | Descrição | Parâmetros | Retorno |
|--------|-----------|------------|---------|
| `validar_cpf(cpf)` | Valida um CPF | `cpf (str)`: CPF com ou sem formatação | `bool`: True se válido |
| `validar_cnpj(cnpj)` | Valida um CNPJ | `cnpj (str)`: CNPJ com ou sem formatação | `bool`: True se válido |
| `formatar_cpf(cpf)` | Formata um CPF | `cpf (str)`: CPF apenas números | `str`: CPF formatado |
| `formatar_cnpj(cnpj)` | Formata um CNPJ | `cnpj (str)`: CNPJ apenas números | `str`: CNPJ formatado |

### Módulo `cep`

| Função | Descrição | Parâmetros | Retorno |
|--------|-----------|------------|---------|
| `buscar_cep(cep)` | Consulta informações do CEP | `cep (str)`: CEP com ou sem formatação | `dict`: Dados do endereço |
| `validar_cep(cep)` | Valida formato do CEP | `cep (str)`: CEP para validar | `bool`: True se válido |
| `formatar_cep(cep)` | Formata um CEP | `cep (str)`: CEP apenas números | `str`: CEP formatado |

### Módulo `formatadores`

| Função | Descrição | Parâmetros | Retorno |
|--------|-----------|------------|---------|
| `formatar_real(valor)` | Formata valor em Real | `valor (float)`: Valor numérico | `str`: Valor formatado |
| `formatar_telefone(telefone)` | Formata número de telefone | `telefone (str)`: Número do telefone | `str`: Telefone formatado |
| `formatar_porcentagem(valor)` | Formata porcentagem | `valor (float)`: Valor decimal | `str`: Porcentagem formatada |

## 🧪 Testes

Execute os testes com:

```bash
python -m pytest tests/
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📋 Roadmap

- [ ] Validação de outros documentos (RG, CNH, etc.)
- [ ] Cálculo de feriados estaduais e municipais
- [ ] Integração com outras APIs de CEP
- [ ] Validação de contas bancárias
- [ ] Formatação de placas de veículos

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Samuel Lucas** - [samuellcs](https://github.com/samuellcs)

## 🙏 Agradecimentos

- [ViaCEP](https://viacep.com.br/) pela API gratuita de consulta de CEP
- Comunidade Python brasileira
- Projeto desenvolvido como parte do bootcamp DIO

---

⭐ Se este projeto te ajudou, considere dar uma estrela no GitHub!