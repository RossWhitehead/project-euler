def execute():
  print("Executing problem 17")

  # one = 3, two = 3, three = 5, four = 4, five = 4, six = 3, seven = 5, eight = 5, nine = 4
  # ten = 3, eleven = 6, twelve = 6, thirteen = 8, fourteen = 8, fifteen = 7, sixteen = 7, seventeen = 9, eighteen = 8, nineteen = 8
  # twenty one = 6 + one, ..............
  # thirty one = 6 + one, ...............
  # forty
  # fifty
  # sixty
  # seventy
  # eighty
  # ninety
  # one hundred and one
  # two hundred 
  # ....
  # one thousand 

  oneToNine = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
  tenToNineteen = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
  twentyToNinetyNine = (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) * 10 + oneToNine * 8
  oneToNinetyNine = oneToNine + tenToNineteen + twentyToNinetyNine
  hundred = 7
  # onehundred * 100 + twohundred * 100... + oneToNinetyNine * 9 + (and * 99 * 9)
  oneHundedToNineHundredAndNinetyNine = (oneToNine + 9 * hundred) * 100 + oneToNinetyNine * 9 + 3 * 99 * 9
  oneThousand = 11

  count = oneToNinetyNine + oneHundedToNineHundredAndNinetyNine + oneThousand
 
  print oneToNine
  print tenToNineteen
  print twentyToNinetyNine
  print oneToNinetyNine
  print oneHundedToNineHundredAndNinetyNine
  print count

execute()


