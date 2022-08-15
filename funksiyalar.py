import random
from anywords import words

def get_word():
  word = random.choice(words)
  while "-" in word or ' ' in word:
    word = random.choice(words)
  return word.upper()

def display(user_letters,word):
  display_letter=""
  for letter in word:
    if letter in user_letters.upper():
      display_letter += letter
    else:
      display_letter += "-"
  return display_letter

def play():
  word = get_word()
  # Sozdagi harflar
  word_letters = set(word)
  #Foydalanuvchi kiritgan harflar
  user_letters = ''
  print(f"Men {len(word)} honali soz oyladim. Topa olasizmi?")
  ##
  while len(word_letters)>0:
    print(display(user_letters, word))
    if len(user_letters)>0:
      print(f"SHu vaqtgacha kiritgan harflarni")
      
    letter = input("Xarf kiriting: ").upper()
    if letter in user_letters:
      print("Bu harfni avval kiritgansiz. Yana urinib koring")
      continue
    elif letter in word:
      word_letters.remove(letter)
      print(f"{letter} xarfi tog'ri.")
    else:
      print("Bunday harf yoq.")
    user_letters += letter
  print(f"Tabriklayman! {word} sozini {len(user_letters)} ta urinishda toptingiz ")

  