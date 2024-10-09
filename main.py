def main():
  source = "books/frankenstein.txt"
  with open(source) as f:
    file_contents = f.read()

  words = file_contents.split()
  number_of_words = len(words)

  char_count = {}
  for char in file_contents.lower():
    char_count[char] = char_count.get(char, 0) + 1

  char_count_list = []
  for key in char_count:
    if key.isalpha():
      char_count_list.append({"name": key, "num": char_count[key]})

  def sort_on(dict):
    return dict["num"]

  char_count_list.sort(reverse=True, key=sort_on)

  print_result(source, number_of_words, char_count_list)


def print_result(source, words, list):
  print(f"--- Begin report of {source} ---")
  print(f"{words} words found in the document")
  print()
  for letter in list:
    print(f"The '{letter["name"]}' character was found {letter["num"]} times")

main()