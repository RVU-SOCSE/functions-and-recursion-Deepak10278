# Word Count Program
#deepak l gowda
#1RUA25BCA0027

def word_count(sentence):
    words = sentence.split()
    return len(words)


text = input("Enter a sentence: ")

count = word_count(text)

print("Total words =", count)
