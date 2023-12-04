def count_words(S):
    word_count = 0
    prev_char = ' '  

    for char in S:
        if char != ' ' and prev_char == ' ':
            word_count += 1
        prev_char = char

    return word_count

S = input()

result = count_words(S)
print(result)