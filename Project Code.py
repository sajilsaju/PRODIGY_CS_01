def caesar_cipher(text, shift, mode='E'):
    result = ""

 if mode == 'D':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = ord(char) + shift_amount

            if char.islower():
                if new_char > ord('z'):
                    new_char -= 26
                elif new_char < ord('a'):
                    new_char += 26
                    
      elif char.isupper():
                if new_char > ord('Z'):
                    new_char -= 26
                elif new_char < ord('A'):
                    new_char += 26

            result += chr(new_char)
        else:
            result += char

    return result

#User input section
message = input("Enter the message here:")
shift_value = int(input("Enter the value that you want to shift: "))
mode = input("Enter mode ('E' for encryption and for decryption press 'D'): ")

#output function
output = caesar_cipher(message, shift_value, mode)
print(f"Output: {output}")
