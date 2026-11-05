# Hill climbing: move to a neighbouring state with a better score.
def score(x):
    return -(x - 7) ** 2 + 30

def hill_climb(start):
    current = start

    while True:
        neighbours = [current - 1, current + 1]
        best = max(neighbours, key=score)

        if score(best) <= score(current):
            return current

        current = best

answer = hill_climb(0)
print("Best state:", answer)
print("Score:", score(answer))
