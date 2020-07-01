#1. Define a function which receives a string as a parameter. The function splits the string into
# pairs of two characters. If the string contains an odd number of characters then it should replace
# the missing second character of the final pair with an underscore ('_').
import textwrap

def despartire_metoda(input):
    despartire = textwrap.wrap(input, 2)
    if len(despartire[-1])==1:
        despartire[-1] += "_"
    return despartire

print(despartire_metoda('abc'))

print(despartire_metoda('abcdef'))

#2. Create a function function that accepts a string parameter, and reverses each word in the string.
# All spaces in the string should be retained.

def reverse_words(text):
  words = []
  for word in text.split(' '):
      word_array = list(word)
      word_array.reverse()
      words.append(str(''.join(word_array)))
  return ' '.join(words)

print(reverse_words("This is an example!"))
print(reverse_words("double  spaces"))