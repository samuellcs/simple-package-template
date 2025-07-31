"""
Testes unitários para o módulo validadores do brasil_utils
"""

import unittest
from brasil_utils.validadores import validar_cpf, validar_cnpj, formatar_cpf, formatar_cnpj


class TestValidadores(unittest.TestCase):
    
    def test_validar_cpf_valido(self):
        """Testa CPFs válidos"""
        cpfs_validos = [
            "123.456.789-09",
            "12345678909",
            "111.444.777-35"
        ]
        
        for cpf in cpfs_validos:
            with self.subTest(cpf=cpf):
                self.assertTrue(validar_cpf(cpf))
    
    def test_validar_cpf_invalido(self):
        """Testa CPFs inválidos"""
        cpfs_invalidos = [
            "123.456.789-10",  # Dígito verificador incorreto
            "11111111111",     # Todos os dígitos iguais
            "123456789",       # Menos de 11 dígitos
            "123456789012",    # Mais de 11 dígitos
            ""                 # String vazia
        ]
        
        for cpf in cpfs_invalidos:
            with self.subTest(cpf=cpf):
                self.assertFalse(validar_cpf(cpf))
    
    def test_validar_cnpj_valido(self):
        """Testa CNPJs válidos"""
        cnpjs_validos = [
            "11.222.333/0001-81",
            "11222333000181"
        ]
        
        for cnpj in cnpjs_validos:
            with self.subTest(cnpj=cnpj):
                self.assertTrue(validar_cnpj(cnpj))
    
    def test_validar_cnpj_invalido(self):
        """Testa CNPJs inválidos"""
        cnpjs_invalidos = [
            "11.222.333/0001-82",  # Dígito verificador incorreto
            "11111111111111",      # Todos os dígitos iguais
            "1122233300018",       # Menos de 14 dígitos
            ""                     # String vazia
        ]
        
        for cnpj in cnpjs_invalidos:
            with self.subTest(cnpj=cnpj):
                self.assertFalse(validar_cnpj(cnpj))
    
    def test_formatar_cpf(self):
        """Testa formatação de CPF"""
        self.assertEqual(formatar_cpf("12345678909"), "123.456.789-09")
        self.assertEqual(formatar_cpf("123.456.789-09"), "123.456.789-09")
        self.assertEqual(formatar_cpf("11111111111"), "")  # CPF inválido
    
    def test_formatar_cnpj(self):
        """Testa formatação de CNPJ"""
        self.assertEqual(formatar_cnpj("11222333000181"), "11.222.333/0001-81")
        self.assertEqual(formatar_cnpj("11.222.333/0001-81"), "11.222.333/0001-81")
        self.assertEqual(formatar_cnpj("11111111111111"), "")  # CNPJ inválido


if __name__ == '__main__':
    unittest.main()
