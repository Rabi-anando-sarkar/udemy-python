# file = open("test.txt", "w")
# try:
#     file.write("Testing file")
# finally:
#     file.close()

with open("order.txt", "w") as file:
    file.write("Testing a new version")