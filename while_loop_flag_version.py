def get_starting_number():
    starting_number = 0
    while starting_number <=0:
        try:
            user_input = input('How many bottles of beer on the wall?')
            stripped_input = user_input.strip()
            starting_number = int(stripped_input)
        except ValueError:
            continue
    return starting_number

def sing(num_bottles):
    while num_bottles > 0:
        if num_bottles > 1:
            bottles_str = 'bottles'
            take_str = 'one'
            if num_bottles-1>1:
                last_verse = f'{num_bottles-1} {bottles_str} of beer on the wall.'
            else:
                last_verse = f'{num_bottles-1} bottle of beer on the wall'
        else:
            bottles_str = 'bottle'
            last_verse = 'no more bottles of beer on the wall!'
            take_str = 'it'
        print(f'{num_bottles} {bottles_str} of beer on the wall, {num_bottles} {bottles_str} of beer.')
        print(f'Take {take_str} down, pass it around, {last_verse}\n')
        num_bottles -= 1