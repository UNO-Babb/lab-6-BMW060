#WordCount.py
#Name: Brennan Wood
#Date: 2/28/25
#Assignment: Lab 5 WordCount

def main():
  file = input("Input file name: ")
  textFile = open(file, 'r')
  
  lineCount = 0
  wordCount = 0
  letterCount = 0
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      for c in w:
        if c.upper() in alpha:
          letterCount = letterCount + 1



  print("Lines: ",lineCount)
  print("Words: ",wordCount)
  print("Characters (including spaces): ",letterCount)


if __name__ == '__main__':
  main()
