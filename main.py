
def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = count_words(text)
  num_letters = count_letters(text)
  list_of_dicts = convert(num_letters)
  list_of_dicts.sort(reverse=True, key=sort_on)
  return(generate_report(list_of_dicts,book_path, num_words))
  


def count_words(text):

  words = text.split()
  count = 0
  for word in words:
    count +=1
  return count


def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
    return file_contents


def count_letters(text):
  lowered_text = text.lower()
  only_letters = ""

  for x in lowered_text:
    if (x.isalpha()) == True:
      only_letters += x

  letters = {}

  for char in only_letters:
    
    if char in letters:
        val = letters[char]
        letters[char] = val+1
    else:
        letters[char] = 1 


  return letters

def sort_on(dict):
    for i in dict:
      return dict[i]

def convert(dictionary):
  return [{key: value} for key, value in dictionary.items()]


def generate_report(dict,book,num_words):
  
  print(f"--- Begin report of {book}---")
  print (f"{num_words} words found in a document")

  for item in dict:
    for i in item.items():
        print(f"The '{i[0]}' character was found {i[1]} times")
  print("---End report---")
    

main()