birthdays = {
    "ali": "02/04/2007",
    "babar": "01/02/2006",
    "abdul": "04/03/2005"
}
print("\nWELCOME TO THE BIRTHDAYS DICTIONARY.WE KNOW THE BIRTHDAYS OF:")
for name in birthdays.keys():
    print(name)
person = input("Whose birthday do you want to look up? ")
if person in birthdays:
    print(person, "birthday is", birthdays[person])
else:
  print("sorry,we don't have that birthday in the dictionary.")
