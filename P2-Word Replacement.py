def replacing_word():
    sentence=input('Enter the sentence here: ')
    word_to_replace=input("Enter the word you want to replace: ")
    word_to_replace_with=input('Enter the word you want to replce with: ')

    print(sentence.replace(word_to_replace,word_to_replace_with))

replacing_word()