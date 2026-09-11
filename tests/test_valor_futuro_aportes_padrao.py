import pytest
from fincalc import calcular_valor_futuro


def test_valor_futuro_aportes_padrao():
    vf = calcular_valor_futuro(500.0, 1.0, 3)
    assert round(vf, 2) == 1530.20


def test_valor_futuro_aporte_negativo():
    with pytest.raises(ValueError):
        calcular_valor_futuro(-500.0, 1.0, 3)
