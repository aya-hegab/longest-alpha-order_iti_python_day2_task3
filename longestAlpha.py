# from userData import userData.isStringOnly

def userInputs():
  userIn = input("enter a string ")
  while userIn.isdigit() or len(userIn) == 0:
    userIn = input("enter a string ")
  myStr = userIn
  return myStr

def longestAlpha(aStr):
  myStr = aStr.lower()
  alphabets="abcdefghijklmnopqrstuvwxyz"
  tmp = ""
  daLongestAlpha = ""
  startchar = 0
  nextchar = 0
  for i in range(len(myStr) - 1):
    startchar = alphabets.index(myStr[i])
    nextchar = alphabets.index(myStr[i + 1]) 
    if nextchar > startchar:
      tmp += myStr[i]
    else:
      tmp += myStr[i]
      # print(tmp)
      # print(daLongestAlpha)
      if len(tmp) > len(daLongestAlpha):
        daLongestAlpha = tmp
      tmp = ""
  print(daLongestAlpha)


longestAlpha("abdulrahman")
# print(isStringOnly("hello"))