def checkleapyear(year):
  if year%4000==0:
    return True
  elif year%4==0:
    if year%100!=0:
      return True
    else:
      return False
year=int(input("ENTER THE YEAR:"))
if(checkleapyear(year)):
  print("LEAP YEAR")
else:
  print("NOT A LEAP YEAR")
      