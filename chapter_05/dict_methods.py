d={}#Empty dictanary
marks={
    "Harry":100,
    "Achinta":90,
    "subham":40,
    0: "harry"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Achinta":99,"Ranuka":55})

print(marks.get("Harry"))
print(marks["Harry"])