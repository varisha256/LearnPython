from sys import argv
script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm {script} script.")
print("I'd like to ask you few questions")

print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of laptop do you have?")
computer = input(prompt)

print(f"So, so said {likes} about liking me, you lives in {lives} and you use {computer} laptop")