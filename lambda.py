fruit = [
    {"name": "watermelon" , "color": "Red"},
    {"name": "banana", "color" : "yellow"},
    {"name": "apple", "color": "green"}
]

fruit.sort(key=lambda fruit: fruit["color"])

print(fruit)