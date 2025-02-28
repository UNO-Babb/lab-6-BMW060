#WordCount.py
#Name: Brennan Wood
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
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      words = words.split()
      for w in words:
        letterCount = letterCount + 1



  print("Lines: ",lineCount)
  print("Words: ",wordCount)
  print("Characters (including spaces): ",letterCount)


if __name__ == '__main__':
  main()
