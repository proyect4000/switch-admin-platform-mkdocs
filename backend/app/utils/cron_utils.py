def parse_simple_cron(expr: str):
    parts = expr.split()
    if len(parts) != 5:
        raise ValueError("Expresión cron inválida")
    minute, hour, day, month, day_of_week = parts
    return {
        "minute": minute,
        "hour": hour,
        "day": day,
        "month": month,
        "day_of_week": day_of_week
    }
