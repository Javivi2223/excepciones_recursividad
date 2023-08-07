def countdown(num):
  if num == 0:
    print("caboom")
  else:
    print(num)
    countdown(num - 1) 

countdown(5)           
