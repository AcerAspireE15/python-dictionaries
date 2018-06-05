people = {"john": 32, "rob": 23}
print(people)
print(people["john"])
print(people["rob"])

numbers = {

    1: "one",
    2: "two",
    3: "three"

}
print(1 in numbers)
print(5 in numbers)
print(numbers.get(2))
print(numbers.get(4))
print(numbers.get(5, "key not found"))
