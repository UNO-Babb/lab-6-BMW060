#WordIndex.py
#Name: Brennan Wood
#Date: 3/1/25
#Assignment: Lab 6 WordIndex

def main():
  file = input("File name: ")
  textFile = open(file, 'r')
  
  words = {} #create an empty dictionary

  lineNum = 0
  for line in textFile:
    lineNum = lineNum + 1
    wordList = line.split()
    for w in wordList:
      w = w.lower()
      w = w.replace("," , "")
      w = w.replace("." , "")
      w = w.replace("-" , "")
      w = w.replace("!" , "")
      w = w.replace("/" , "")

      if w in words:
        if lineNum not in words[w]:
          words[w].append(lineNum)
      else:
         words[w] = [lineNum]

  for w in words:
    print(w, words[w])



if __name__ == '__main__':
  main()