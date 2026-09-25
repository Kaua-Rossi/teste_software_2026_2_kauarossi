from backend.entity.produto import Produto
import pytest
from backend.exceptions.excecoes import CampoVazioError

def test_criar_produto_com_sucesso():
    """Garante que o Produto seja criado com dados válidos."""
    cafe = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert cafe._nome == "cafe"
    assert cafe._preco == 18 and cafe._quant_estoque == 50 and \
        cafe._validade == 3 and cafe._codigo_barras == 1234567890 and \
        cafe._categoria == "alimenticio" and cafe._peso == 250

def test_criar_produto_sem_nome():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(CampoVazioError):
        Produto("", 18, 50, 3, 1234567890, "alimenticio", 250)

def test_criar_produto_sem_preco():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(CampoVazioError):
        Produto("cafe", None, 50, 3, 1234567890, "alimenticio", 250)

def test_criar_produto_sem_quant_estoque():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(CampoVazioError):
        Produto("cafe", 18, None, 3, 1234567890, "alimenticio", 250)

def test_criar_produto_sem_validade():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(CampoVazioError):
        Produto("cafe", 18, 50, None, 1234567890, "alimenticio", 250)

def test_criar_produto_sem_codigo_barras():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(CampoVazioError):
        Produto("cafe", 18, 50, 3, None, "alimenticio", 250)

def test_criar_produto_sem_categoria():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(CampoVazioError):
        Produto("cafe", 18, 50, 3, 1234567890, "", 250)

def test_criar_produto_sem_peso():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(CampoVazioError):
        Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", None)

def test_getter_produto_nome():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert p.nome == "cafe"

def test_setter_produto_nome():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    p.nome = "cafe"
    assert p.nome == "cafe"

def test_getter_produto_preco():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert p.preco == 18

def test_setter_produto_preco():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    p.preco = 18
    assert p.preco == 18

def test_getter_produto_quant_estoque():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert p.quant_estoque == 50

def test_setter_produto_quant_estoque():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    p.quant_estoque = 50
    assert p.quant_estoque == 50

def test_getter_produto_validade():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert p.validade == 3

def test_setter_produto_validade():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    p.validade = 3
    assert p.validade == 3

def test_getter_produto_codigo_barras():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert p.codigo_barras == 1234567890

def test_setter_produto_codigo_barras():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    p.codigo_barras = 1234567890
    assert p.codigo_barras == 1234567890

def test_getter_produto_categoria():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert p.categoria == "alimenticio"

def test_setter_produto_categoria():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    p.categoria = "alimenticio"
    assert p.categoria == "alimenticio"

def test_getter_produto_peso():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert p.peso == 250

def test_setter_produto_peso():
    p = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    p.peso = 250
    assert p.peso == 250