visitors = {}
name = input("Hello! What's your name?\n")
age = input(f"Great! Welcome, {name}! How old are you?\n")
visitors[name] = age
print(f"Visitor log: {visitors}")