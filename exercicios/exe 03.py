def calculate_withdrawal_options():
    name = input("Nome Completo: ")
    admission_date = input("Data de admisão (YYYY-MM-DD): ")
    current_salary = float(input("Salário atual: "))
    loan_amount = int(input("Valor de empréstimo: "))

    if (loan_amount % 2) != 0:
        print("Por favor entre com um valor válido!: ")
        return

    years_employed = 2023 - int(admission_date[:4])

    if years_employed < 5:
        print("Obrigado pelo seu interesse, mas você não atende aos requisitos mínimos do programa.")
        return

    if loan_amount > (2 * current_salary):
        print("O valor do empréstimo excede o limite máximo.")
        return

    higher_value_notes = []
    lower_value_notes = []
    half_and_half_notes = []

    higher_value = loan_amount // 100
    higher_value_notes.append(f"{higher_value} x 100 reais")
    loan_amount -= higher_value * 100

    if loan_amount >= 50:
        higher_value_notes.append("1 x 50 reais")
        loan_amount -= 50

    while loan_amount >= 20:
        lower_value_notes.append("1 x 20 reais")
        loan_amount -= 20

    if loan_amount >= 10:
        lower_value_notes.append("1 x 10 reais")
        loan_amount -= 10

    while loan_amount >= 5:
        lower_value_notes.append("1 x 5 reais")
        loan_amount -= 5

    higher_value = loan_amount // 100
    if higher_value > 0:
        half_and_half_notes.append(f"{higher_value} x 100 reais")
        loan_amount -= higher_value * 100

    if loan_amount >= 50:
        half_and_half_notes.append("1 x 50 reais")
        loan_amount -= 50

    while loan_amount >= 20:
        half_and_half_notes.append("1 x 20 reais")
        loan_amount -= 20

    if loan_amount >= 10:
        half_and_half_notes.append("1 x 10 reais")
        loan_amount -= 10

    while loan_amount >= 5:
        half_and_half_notes.append("1 x 5 reais")
        loan_amount -= 5

    print("\nMontante do empréstimo:", loan_amount)
    print("Notas de maior valor:")
    for note in higher_value_notes:
        print(note)

    print("\nNotas de menor valor:")
    for note in lower_value_notes:
        print(note)

    print("\nMeias e meias notas:")
    print(f"{loan_amount} reais em notas de maior valor:")
    for note in half_and_half_notes:
        print(note)

    print(f"{loan_amount} reais em notas de menor valor:")
    for note in lower_value_notes:
        print(note)


calculate_withdrawal_options()