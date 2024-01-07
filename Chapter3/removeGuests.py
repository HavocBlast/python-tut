guest_list = ['Mike', 'Mark', 'John', 'Jane', 'Smith', 'Jennifer', 'Mike', 'Jane', 'Jane']

print('You can only invite two people')

while len(guest_list) > 2:
    guest = guest_list.pop()
    print(f'I am sorry but I cannot invite you, {guest}')

for guest_left in guest_list:
    print(f'Hi {guest_left}, I would like to invite you to dinner!')
    del guest_list[0:2]
print(guest_list)