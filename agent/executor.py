def check_scheme(age, income):
    print("Executor running with:", age, income)

    if age >= 18 and income <= 200000:
        return "PM Kisan పథకం"
    else:
        return None
