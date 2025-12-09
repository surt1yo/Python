#Write a Python class to reverse a string word by word.
class StringReverser:
    def reverse_words(self, sentence: str) -> str:
        words = [word for word in sentence.split() if word]
        return ' '.join(reversed(words))
input_sentence = input("Enter a sentence: ")
reverser = StringReverser()
print(reverser.reverse_words(input_sentence))
