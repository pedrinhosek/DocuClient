
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
