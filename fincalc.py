"""FinCalc - Sistema de Cálculos Financeiros em Python."""

__version__ = "1.0.0"


def calcular_juros_simples(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_juros_compostos(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros compostos."""
    if capital < 0:
        raise ValueError("O capital não pode ser negativo.")
    if anos < 0:
        raise ValueError("O tempo em anos não pode ser negativo.")
    montante = capital * ((1 + (taxa_anual / 100)) ** anos)
    return montante


def calcular_aposentadoria(
    patrimonio_atual: float,
    aporte_mensal: float,
    anos: int,
    taxa_anual: float,
) -> float:
    """Calcula o patrimônio acumulado para aposentadoria."""
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual
    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)
    return saldo


def calcular_parcela_price(
    valor_emprestimo: float,
    taxa_mensal: float,
    meses: int,
) -> float:
    """Calcula o valor da parcela fixa em um financiamento pela Tabela Price."""
    if valor_emprestimo < 0:
        raise ValueError("Valor do empréstimo não pode ser negativo.")
    if meses <= 0:
        raise ValueError("Número de meses deve ser maior que zero.")
    i = taxa_mensal / 100
    if i == 0:
        return valor_emprestimo / meses
    fator = (1 + i) ** meses
    parcela = valor_emprestimo * (i * fator) / (fator - 1)
    return parcela


if __name__ == "__main__":
    print("Iniciando o sistema FinCalc...")
    montante = calcular_juros_simples(1000.0, 5.0, 2)
    print(f"Juros Simples: R$ {montante:.2f}")
    montante_comp = calcular_juros_compostos(1000.0, 5.0, 2)
    print(f"Juros Compostos: R$ {montante_comp:.2f}")
    patrimonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    print(f"Patrimônio Estimado para Aposentadoria: R$ {patrimonio:.2f}")
    parcela = calcular_parcela_price(50000.0, 1.2, 48)
    print(f"Parcela Fixa (Tabela Price): R$ {parcela:.2f}")


def calcular_rendimento_real(ganho_nominal: float, inflacao: float) -> float:
    """Calcula a taxa de retorno real descontada a inflação do período."""

    if inflacao == -100.0:
        raise ValueError("A inflação não pode ser igual a -100%, pois causa divisão por zero.")

    retorno_real = ((1 + (ganho_nominal / 100)) / (1 + (inflacao / 100))) - 1
    return retorno_real * 100


def converter_taxa_anual_para_mensal(taxa_anual: float) -> float:
    """Converte uma taxa de juros anual equivalente para taxa mensal."""
    if taxa_anual < -100:
        raise ValueError("A taxa anual não pode ser menor que -100")
    return (((1 + (taxa_anual / 100)) ** (1 / 12)) - 1) * 100


def calcular_irrf(salario_bruto: float) -> float:
    """Calcula a alíquota simplificada de Imposto de Renda Retido na Fonte."""
    if salario_bruto < 0:
        raise ValueError("Salário bruto não pode ser negativo.")
    if salario_bruto <= 2259.20:
        return 0.0
    if salario_bruto <= 2826.65:
        return (salario_bruto * 0.075) - 169.44
    if salario_bruto <= 3751.05:
        return (salario_bruto * 0.15) - 381.44
    return (salario_bruto * 0.225) - 662.77


def calcular_margem_liquida(receita_total: float, custos_totais: float) -> float:
    """Calcula a margem de lucro líquida percentual de uma operação."""
    lucro = receita_total - custos_totais
    return (lucro / receita_total) * 100


def calcular_valor_futuro(
    aporte_mensal: float, taxa_mensal: float, meses: int
) -> float:
    """Calcula o valor futuro acumulado com aportes mensais recorrentes."""
    i = taxa_mensal / 100
    vf = aporte_mensal * (((1 + i) ** meses - 1) / i)
    return vf


def calcular_depreciacao_linear(
    valor_inicial: float,
    valor_residual: float,
    vida_util_anos: int,
) -> float:
    """Calcula o valor de depreciação anual de um ativo corporativo."""

    if vida_util_anos <= 0:
        raise ValueError("A vida útil deve ser maior que zero.")

    if valor_residual > valor_inicial:
        raise ValueError(
            "O valor residual não pode ser maior que o valor inicial."
        )

    return (valor_inicial - valor_residual) / vida_util_anos

