# # Executes code
# # Try something that might cause an exception
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
#
# # Execute try statement catches any the error stated.
# # Do this if there was an exception
# except FileNotFoundError:
#     file = open("a_file.txt", "a")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
#
# # Do this if there were no exceptions
# else:
#     content = file.read()
#     print(content)
#
# # Executes statement in case try statement in both cases whether it was successful or not
# # Do this no matter what happens
# finally:
#     # file.close()
#     # print("File was closed ")
#     # Raise is used to raise an exception
#     raise KeyError("Nu e bun ba")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)