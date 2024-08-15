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
    print(f'\nPlease enter your message to {mode}. ')
    message = input('>: ')
    return message


def encrypt_decrypt_message(input_message: str, symbols: str, input_key: int, mode: str):
    encrypted_msg = ''
    input_message = input_message.upper()
    for letter in input_message:
        if letter in symbols:
            letter_index = symbols.find(letter)

            if mode == 'encrypt':
                if letter_index + input_key > len(symbols):
                    letter_index = (letter_index + input_key) - len(symbols)
                else:
                    letter_index = letter_index + input_key
            elif mode == 'decrypt':
                if letter_index - input_key <= 0:
                    letter_index = (letter_index - input_key) + len(symbols)
                else:
                    letter_index = letter_index - input_key
            encrypted_msg += symbols[letter_index]

        else:
            encrypted_msg += letter
    return encrypted_msg


def main():
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while True:
        input_mode = get_user_command()
        if input_mode is not None:
            input_key = get_user_key(len(symbols))
            if input_key is not None:
                input_message = get_user_message(input_mode)
                e_message = encrypt_decrypt_message(input_message, symbols, input_key, input_mode)
                print(e_message)
            else:
                print('You did not enter a valid key!')
        else:
            print('You did not enter a valid mode!')
        input_answer = input('Do you wish to continue? [Y/N]').lower()
        if input_answer == 'n':
            print('See you soon. Bye')
            break


main()
