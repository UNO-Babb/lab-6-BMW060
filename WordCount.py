#WordCount.py
#Name: Brennan Wood
#Date: 2/28/25
#Assignment: Lab 6 WordCount

def main():
  file = input("Input file name: ")
  textFile = open(file, 'r')
  
  lineCount = 0
  wordCount = 0
  letterCount = 0

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      for c in w:
        letterCount = letterCount + 1



  print("Lines: ",lineCount)
  print("Words: ",wordCount)
  print("Characters (not including spaces): ",letterCount)


if __name__ == '__main__':
  main()
