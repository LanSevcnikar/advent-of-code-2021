with open('in.txt') as openfileobject:
  values = []
  for line in openfileobject:
    values.append([char for char in line][0:-1])

  gamma = ""
  epsilon = ""

  oxvalues = values[:]
  covalues = values[:]

  for i in range(len(values[0])):
    ones = 0
    zeros = 0

    oxones = 0
    oxzeros = 0
    coones = 0
    cozeros = 0

    for data in values:
      if(data[i] == "1"):
        zeros += 1
      else:
        ones += 1
      
    for data in oxvalues:
      if(data[i] == "1"):
        oxzeros += 1
      else:
        oxones += 1
      
    for data in covalues:
      if(data[i] == "1"):
        cozeros += 1
      else:
        coones += 1

    if(ones > zeros):
      gamma += "0"
      epsilon += "1"
    else:
      gamma += "1"
      epsilon += "0"

    if(oxones > oxzeros):
      if(len(oxvalues) > 1):
        oxvalues = [item for item in oxvalues if item[i] == "0"]
    else:
      if(len(oxvalues) > 1):
        oxvalues = [item for item in oxvalues if item[i] == "1"]
      
    if(coones > cozeros):
      if(len(covalues) > 1):
        covalues = [item for item in covalues if item[i] == "1"]
    else:
      if(len(covalues) > 1):
        covalues = [item for item in covalues if item[i] == "0"]
      

  print(int("".join(oxvalues[0]),2) , int("".join(covalues[0]),2))
  print(int("".join(oxvalues[0]),2) * int("".join(covalues[0]),2))

  print(int(gamma,2) * int(epsilon,2))
