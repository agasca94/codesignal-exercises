def currencyArbitrage(exchange):
    V = len(exchange)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist = max(
                    1 * exchange[i][j],
                    1 * exchange[i][k] * exchange[k][j]
                )
                exchange[i][j] = dist
                if exchange[i][j] * exchange[j][i] > 1:
                    return True

    return False
