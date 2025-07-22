from Modules.user import UserFront
from Modules.chat import Chat
CB = Chat("Rizwan")
print(CB.greet())
query = input()

print(CB.queryset(query))
