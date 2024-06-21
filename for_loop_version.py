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
    for i in range(num_bottles):
        remain_bottles = num_bottles - i
        if remain_bottles > 1:
            bottles_str = 'bottles'
            take_str = 'one'
            if remain_bottles-1>1:
                last_verse = f'{remain_bottles-1} {bottles_str} of beer on the wall.'
            else:
                last_verse = f'{remain_bottles-1} bottle of beer on the wall'
        else:
            bottles_str = 'bottle'
            last_verse = 'no more bottles of beer on the wall!'
            take_str = 'it'
        print(f'{remain_bottles} {bottles_str} of beer on the wall, {remain_bottles} {bottles_str} of beer.')
        print(f'Take {take_str} down, pass it around, {last_verse}\n')
