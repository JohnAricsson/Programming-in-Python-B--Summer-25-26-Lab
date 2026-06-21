from collections import Counter
d = {
    'A': 10,
    'B': 10,
    'C': 40,
    'D': 20,
    'E': 70,
    'F': 80,
    'G': 40,
    'H': 20
}
freq = Counter(d.values())
print(freq)