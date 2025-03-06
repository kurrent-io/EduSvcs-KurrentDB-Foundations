import hashlib

with open('hashed_solution.txt', 'r') as file:
     file_content = file.read()
hash_solution = file_content

while True:
    try:
        guess = (input("How many events were written? "))
        hash_guess = (hashlib.md5(str(guess).encode('utf-8')).hexdigest())
        if hash_guess != hash_solution:
            raise ValueError("Wrong Answer please try again: ")
        break
    except ValueError:
        print("Wrong Answer please try again")


print("Great work, you are correct")

