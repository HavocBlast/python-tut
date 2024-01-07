guest_list = ['Mike', 'Mark', 'John', 'Jane', 'Smith']

for guest in guest_list:
    print(f'Hi {guest}! You are invited to dinner at my place')

print(f'{guest_list[3]} cannot make it to dinner.')

guest_list.remove(guest_list[3])
guest_list.append('Kim')

for guest in guest_list:
    print(f'Hi {guest}! You are invited to dinner at my place')

guest_list.insert(2,'Jennifer')
guest_list.insert(0, 'James')
guest_list.append('Karl')

for guest in guest_list:
    print(f'Hi {guest}! You are invited to dinner tonight')