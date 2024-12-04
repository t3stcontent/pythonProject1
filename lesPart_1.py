"""key = "+4444"

if key in users:
    user = users[key]
    print(user)
else:
    print("element not found")"""

"""user1 = users.get("+1111")
print(user1)
user2 = users.get("+3333", "Unknown user")
print(user2)
if "+4444" in users:
    del users["+4444"]
print(users)"""

"""key = "+1111121"
user = users.pop(key, "not found")
print(user)
print(users)
users.clear()
print(users)"""

users1 = {"+1111" : "Tom","+2222" : "Bob"}
users2 = {"+3333" : "Sam","+4444" : "Kate"}

#students = users1.copy()
users1.update(users2)

for key, item in users1.items():
    print(f"number : {key} Name: {item}")

for key in users1.keys():
    print(key)

for value in users1.values():
    print(value)