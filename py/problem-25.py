lookup = [0] * (3)

def execute():
  
  nminus2 = 1
  nminus1 = 1

  seq = 2

  while len(str(n)) < 1000:
    n = nminus1 + nminus2
    nminus2 = nminus1
    nminus1 = n

    seq += 1

  print(seq)

execute()