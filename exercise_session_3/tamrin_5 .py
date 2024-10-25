def fibonacci_sequence(n):
    sequence = [1, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]
n = int(input("tedad adad donbale fibonacci: "))
print(fibonacci_sequence(n))