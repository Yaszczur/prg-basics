sentence = 'I completely agree with you'

words = sentence.split() 

result_map = map(lambda word: len(word), words)

result = list(result_map)

print(f"Text: {sentence}")
print(f"No. of letters in words: {result}")