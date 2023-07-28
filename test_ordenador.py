import ordenador
import pytest
import conta_tempo

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()
    
    @pytest.fixture
    def l_quase(self):
        c = conta_tempo.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c = conta_tempo.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True
    
    def test_bolha_curta_aleat(self, o, l_aleat):
        o.bolha_curta(l_aleat)
        assert self.esta_ordenada(l_aleat)