Stack = {}
def holdInfoInStack(name : str, age :str , country : str, option: str):
Stack[name.lower()] = [name , age , country , option]
#print("Information is holded")
def divider(n=20):
print('-' * n)


def displayInfo(name : str, age :str , country : str) -> tuple:
holdInfoInStack(name, age, country, 1)
return name , age , country
def displayInfoByInput(name : str, age :str , country : str) -> tuple:
holdInfoInStack(name, age, country, 2)
return displayInfo(name, age, country)
if __name__ == '__main__':
divider()
# simulate one
name="ESMT"
age=30
country="Mali"
print(displayInfo(name, age, country))
print("\n")



divider()
# simulate two
name2 = input("Entrer un nom: ")
age2 = int(input("Entrer un age: "))
country2 = input("Entrer un pays: ")
print(displayInfoByInput(name2, age2, country2))
