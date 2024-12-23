def get_user_command():
    max_try = 3
    for attempt in range(max_try):
        print('\nDo you want to (e)ncrypt or (d)ecrypt?')
        response = input('>: ').lower()
        if response in ('e', 'd'):
            return 'encrypt' if response == 'e' else 'decrypt'
        else:
            if attempt < max_try - 1:
                print("Please enter 'e' or 'd'.")
                print(f'You have {max_try - attempt - 1} more attempts.')
            else:
                print('Sorry, you did not enter a valid letter.')
    return None


def get_user_key(symbol_len: int):
    max_try = 3

    for attempt in range(max_try):
        print(f'\nPlease enter a number between 1 and {symbol_len - 1}: ')
        response = input('>: ')
        if response.isdigit():
            key = int(response)
            if 0 < key < symbol_len:
                return key
        if attempt < max_try - 1:
            print('Please enter a valid number.')
            print(f'You have {max_try - attempt - 1} more times to try.')
        else:
            print('Sorry! Bye!')
    return None


def get_user_message(mode: str):
    return input(f'\nPlease enter your message to {mode}: ')


def encrypt_decrypt_message(input_message: str, symbols: str, input_key: int, mode: str) -> str:
    result = []
    for letter in input_message:
        if letter.lower() in symbols:
            index = symbols.find(letter.lower())
            shifted_index = (index + input_key) % len(symbols) if mode == 'encrypt' else (index - input_key) % len(symbols)
            new_char = symbols[shifted_index]
            result.append(new_char.upper() if letter.islower() else new_char.lower())
        else:
            result.append(letter)
    return ''.join(result)


def main():
    symbols = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        input_mode = get_user_command()
        if input_mode:
            input_key = get_user_key(len(symbols))
            if input_key:
                input_message = get_user_message(input_mode)
                if input_message:
                    e_message = encrypt_decrypt_message(input_message, symbols, input_key, input_mode)
                    print(f'\nThe result is: {e_message}')
                else:
                    print('Message empty !!!')
            else:
                print('You did not enter a valid key!')
        else:
            print('You did not enter a valid mode!')
        if input('Do you wish to continue? [Y/N] ').lower() == 'n':
            print('See you soon. Bye')
            break


main()
