# Word Count Program
#deepak l gowda
#1RUA25BCA0027

def word_count(sentence):
    count = 0
    in_word = False

    for ch in sentence:
        if ch != " " and in_word == False:
            count += 1
            in_word = True
        elif ch == " ":
            in_word = False

    return count


text = input("Enter a sentence: ")

print("Total words =", word_count(text))
