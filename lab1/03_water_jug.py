from collections import deque

def water_jug(capacity_a, capacity_b, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            return path

        # Fill either jug, empty either jug, or pour water between jugs.
        pour_a_to_b = min(a, capacity_b - b)
        pour_b_to_a = min(b, capacity_a - a)

        next_states = [
            (capacity_a, b),
            (a, capacity_b),
            (0, b),
            (a, 0),
            (a - pour_a_to_b, b + pour_a_to_b),
            (a + pour_b_to_a, b - pour_b_to_a)
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    return None

if __name__ == "__main__":
    solution = water_jug(4, 3, 2)
    if solution:
        for step, state in enumerate(solution):
            print(f"Step {step}: Jug A = {state[0]}L, Jug B = {state[1]}L")
    else:
        print("No solution exists for these jug sizes and target.")
