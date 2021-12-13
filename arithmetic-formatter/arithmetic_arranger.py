def arithmetic_arranger(problems, arg=False):
  s = []
  l = []
  k = []
  o = []

  #return error if more than 5
  if len(problems) >5:
    return "Error: Too many problems."

  for numbers in problems:
    #split input
    number = numbers.split(" ")
    n1 = number[0]
    n2 = number[2]
    operator = number[1]

    #error messages
    if not n1.isdigit() or not n2.isdigit():
      return "Error: Numbers must only contain digits."
    if len(n1) > 4 or len(n2) > 4:
      return "Error: Numbers cannot be more than four digits."
    if "*" in operator or "/" in operator:
      return "Error: Operator must be '+' or '-'."

    #find length of spaces
    spaces = 0
    if len(n1) >= len(n2):
      spaces = len(n1)+2
    else:
      spaces = len(n2)+2

  #make lists with numbers and spaces
    s.extend(((" "*(spaces-len(n1))), n1, "    "))
    l.extend((operator, (" "*(spaces-1-len(n2))), n2, "    "))
    k.extend((("-"*(spaces)), "    "))
   
    #if arg set to True
    if arg:
      if operator == "+":
        u = int(n1) + int(n2)
      else:
        u = int(n1) - int(n2)
      o.extend((" "*(spaces-len(str(u))), str(u), "    "))

  #add lines together plus \n
  for i in range(len(n1)):
    arranged_problems = "".join(s).rstrip(" ") +  "\n" + "".join(l).rstrip(" ") + "\n" + "".join(k).rstrip(" ")
    if arg:
      arranged_problems += "\n" + "".join(o).rstrip(" ")

  return arranged_problems