new_item=input('Whats your new item?')
with open('to do.txt', 'r') as text_file:
    to_do_list = text_file.read()
print(to_do_list)

to_do_list = to_do_list + new_item + 'n'

with open('to do.txt', 'w+') as text_file:
    text_file.write(to_do_list)