# utils/candlestick_patterns.py

def detect_patterns(candles):
    patterns = []
    for i in range(1, len(candles)):
        prev = candles[i - 1]
        curr = candles[i]

        # Extract OHLC for previous and current candle
        o1, h1, l1, c1 = prev['open'], prev['high'], prev['low'], prev['close']
        o2, h2, l2, c2 = curr['open'], curr['high'], curr['low'], curr['close']

        pattern = None

        # Bullish Engulfing
        if c1 < o1 and c2 > o2 and o2 < c1 and c2 > o1:
            pattern = {
                'type': 'Bullish Engulfing',
                'index': i,
                'candle': curr
            }

        # Bearish Engulfing
        elif c1 > o1 and c2 < o2 and o2 > c1 and c2 < o1:
            pattern = {
                'type': 'Bearish Engulfing',
                'index': i,
                'candle': curr
            }

        # Hammer (bullish reversal)
        body = abs(c2 - o2)
        lower_shadow = o2 - l2 if o2 > c2 else c2 - l2
        upper_shadow = h2 - c2 if c2 > o2 else h2 - o2

        if body > 0 and lower_shadow > 2 * body and upper_shadow < body:
            pattern = {
                'type': 'Hammer',
                'index': i,
                'candle': curr
            }

        if pattern:
            patterns.append(pattern)

    return patterns
