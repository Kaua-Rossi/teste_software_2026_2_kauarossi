class CampoVazioError(Exception):
    """Lançada quando um ou mais campos estão vazios/inválidos."""

    def __init__(self,msg):
        """Armazena a mensagem de erro."""
        self.msg = msg

    def __str__(self):
        """Retorna a mensagem de erro como texto."""
        return self.msg
