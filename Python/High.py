"""Encuentra la palabra con la puntuación más alta en una cadena.

  Args:
    cadena: Una cadena de palabras.

  Returns:
    La palabra con la puntuación más alta. Si hay empates, devuelve la primera.
"""
def high(x):
    puntuaciones = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
                 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
                 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    words = x.split()
    max_score = 0
    word = words[0]
    
    for w in words:
        score = sum(puntuaciones[c] for c in word)
        if score > max_score:
            score = max_score
            word = w
        elif score == max_score:
            if words.index(w) < words.index(word):
                word = w
    return w
print(high("ubud taxi"))
