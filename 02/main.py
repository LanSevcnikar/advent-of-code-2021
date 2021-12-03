

with open('in.txt') as openfileobject:
  depth = 0
  dist = 0
  aim = 0
  for line in openfileobject:
    value = int(line.split(" ")[1])
    tp = line.split(" ")[0]
    if(tp == "forward"):
      dist += value
      depth += value * aim
    if(tp == "down"):
      aim += value
    if(tp == "up"):
      aim -= value
  print(depth * dist) 