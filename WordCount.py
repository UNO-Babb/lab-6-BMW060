#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  file = input("Input file name: ")
  textFile = open(file, 'r')
  
  lineCount = 0
  wordCount = 0
  characterCount = 0
  letterCount = 0

  for line in textFile:
    lineCount = lineCount +1
    words = line.split(" ")
    for w in words:
      wordCount = wordCount + 1

  for c in line:
    characterCount = characterCount + 1

  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # borrowed this from Caesar Cipher to count actual letters
  for c in line:
    c = c.upper()
    if c in alpha:
      letterCount = letterCount + 1


  print("Lines: ",lineCount)
  print("Words: ",wordCount)
  print("Characters (including spaces): ",letterCount)
  print("Characters (not including spaces): ",letterCount)


if __name__ == '__main__':
  main()
