vowels = ["a" ,"e", "i", "o", "u"]

def num_vowel():
  counter = 0
  word = str(input("Enter a word: "))
  for vowel in vowels:
    if vowel in word:
      counter += 1

  print("Number of Vowels:", counter)

def main():
  num_vowel()
      

main()
