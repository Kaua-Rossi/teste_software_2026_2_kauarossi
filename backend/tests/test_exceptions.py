import pytest
from backend.exceptions.excecoes import CampoVazioError

def test_campo_vazio_error_str():
    e = CampoVazioError("Mensagem teste")
    assert e.__str__() == "Mensagem teste"