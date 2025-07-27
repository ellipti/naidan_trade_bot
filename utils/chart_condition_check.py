def chart_condition_check(rates):
    if len(rates) < 10:
        return False

    highs = [r.high for r in rates]
    lows = [r.low for r in rates]

    latest_range = highs[-1] - lows[-1]
    avg_range = sum([highs[i] - lows[i] for i in range(-6, -1)]) / 5

    if latest_range > avg_range * 1.5:
        return True
    return False
