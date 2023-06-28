


def userinput():
  bill_prompt = str(input("How much is the bill? "))
  people_prompt = int(input("How many people are in your party? "))

  bill_val = float(bill_prompt[1:len(bill_prompt)])

  each_person_owes = str(bill_val / people_prompt)

  print("Each person owes", "$" + each_person_owes)


userinput()


