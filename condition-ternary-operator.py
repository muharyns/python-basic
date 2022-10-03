passed = False
word = "congratulation" if passed else "Try again"  # ternary
print(word)

passed = True
word = ("try again", "conglatulation")[passed]  # ternary with tuple
print(word)

passed = False
print(passed and "congratulation" or "try again")  # ternary with or