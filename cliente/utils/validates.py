
def cpf_verification(cpf):
    if not cpf or len(cpf) < 11:
        return False

    cpf_block = [str(i) * 11 for i in range(10)]

    if cpf in cpf_block:
        return False

    antigo_cpf = [int(d) for d in cpf]  # Remove verification digits
    novo_cpf = antigo_cpf[:9]

    # Generates new verification digits
    while len(novo_cpf) < 11:
        resto = sum([v * (len(novo_cpf) + 1 - i) for i, v in enumerate(novo_cpf)]) % 11
        digito_verificador = 0 if resto <= 1 else 11 - resto
        novo_cpf.append(digito_verificador)

    if novo_cpf == antigo_cpf:
        return cpf

    return False


def cnpj_verification(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))  # Remove caracteres não numéricos
    if len(cnpj) != 14:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    peso = 5
    for i in range(12):
        soma += int(cnpj[i]) * peso
        peso -= 1
        if peso < 2:
            peso = 9
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Calcula o segundo dígito verificador
    soma = 0
    peso = 6
    for i in range(13):
        soma += int(cnpj[i]) * peso
        peso -= 1
        if peso < 2:
            peso = 9
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    return not cnpj[-2:] == f"{digito1}{digito2}"


def ddd_brasil():
    # Centro-Oeste
    distrito_federal = [61]
    goias = [62, 64]
    mato_grosso = [65, 66]
    mato_grosso_do_sul = [67]
    # Nordeste
    alagoas = [82]
    bahia = [71, 73, 74, 75, 77]
    ceara = [85, 88]
    maranhao = [98, 99]
    paraiba = [83]
    pernambuco = [81, 87]
    piaui = [86, 89]
    rio_grande_do_norte = [84]
    sergipe = [79]
    # Norte
    acre = [68]
    amapa = [96]
    amazonas = [92, 97]
    para = [91, 93, 94]
    rondonia = [69]
    roraima = [95]
    tocantins = [63]
    # Sudeste
    espirito_santo = [27, 28]
    minas_gerais = [31, 32, 33, 34, 35, 37, 38]
    rio_de_janeiro = [21, 22, 24]
    sao_paulo = [11, 12, 13, 14, 15, 16, 17, 18, 19]
    # Sul
    parana = [41, 42, 43, 44, 45, 46]
    rio_grande_do_sul = [51, 53, 54, 55]
    santa_catarina = [47, 48, 49]

    centro_oeste = distrito_federal + goias + mato_grosso + mato_grosso_do_sul
    nordeste = alagoas + bahia + ceara + maranhao + paraiba + pernambuco + piaui + rio_grande_do_norte + sergipe
    norte = acre + amapa + amazonas + para + rondonia + roraima + tocantins
    sudeste = espirito_santo + minas_gerais + rio_de_janeiro + sao_paulo
    sul = parana + rio_grande_do_sul + santa_catarina

    return centro_oeste + nordeste + norte + sudeste + sul
