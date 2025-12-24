def plan(user_text, memory):
    if "age" not in memory:
        return "ASK_AGE"
    if "income" not in memory:
        return "ASK_INCOME"
    return "CHECK_SCHEME"
