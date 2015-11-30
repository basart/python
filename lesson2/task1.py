def countWords(text, words):
    text = text.lower()
    count = 0
    for word in words:
        if word in text:
            count += 1
    return count

print(countWords('How how aregdfg you', set(['how', 'are', 'you'])))
print(countWords('', set()))
