def get_user_command():
    max_try = 3

    for attempt in range(max_try):
        print('\nDo you want to (e)ncrypt or (d)ecrypt?')
        response = input('>: ').lower()

        if response in ('e', 'd'):
            mode = 'encrypt' if response == 'e' else 'decrypt'
            return mode
        else:
            if attempt < max_try - 1:
                print("Please enter the letter 'e' or 'd'.")
                print(f'You have {max_try - attempt - 1} more attempts.')
            else:
                print('Sorry, you did not enter a valid letter.')
    return None


def get_user_key(symbol_len: int):
    max_try = 3
    max_key = symbol_len - 1

    for attempt in range(max_try):
        print(f'\nPlease enter a number between {0} and {max_key}: ')
        response = input('>: ')

        if not response.isdecimal() or not (0 < int(response) <= max_key):
            if attempt == max_try - 1:
                print('Sorry! Bye!')
            else:
                print('Please enter a valid number')
                print(f'You have {max_try - attempt - 1} more times to try.')
        else:
            key = int(response)
            return key
    return None


def get_user_message(mode: str):
    print(f'Please enter your message to {mode}. ')
    message = input('>: ')
    return message


def main():
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols_len = len(symbols)
    encrypted_msg = ''

    while True:
        input_mode = get_user_command()
        if input_mode is not None:
            input_key = get_user_key(symbols_len)
            if input_key is not None:
                input_message = get_user_message(input_mode)
                # print(input_message)
                for letter in input_message:
                    if letter in symbols:
                        letter_index = symbols.find(letter)
                        if letter_index + input_key > len(symbols):
                            new_letter_index = (letter_index + input_key) - len(symbols)
                        else:
                            new_letter_index = letter_index + input_key
                        encrypted_msg += symbols[new_letter_index]
                    else:
                        encrypted_msg += letter
                print(encrypted_msg)
            else:
                print('The key you entered is not valid.')
        else:
            print('The mode you entered is  not valid')
        input_answer = input('Do you wish to continue? [Y/N]').lower()
        if input_answer == 'n':
            print('See you soon. Bye')
            break


main()
