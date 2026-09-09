hour=int(input("entre your input"))
minute=int(input("entre your input"))
second=int(input("entre your input"))

if hour>=0 and hour<=23:
  if minute>=0 and minute<=59:
    if second>=0 and minute<=59:
       print("valid time")
else :
    print("time is valid")    
