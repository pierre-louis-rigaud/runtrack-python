def caesar_encrypt(shift, message):
    encrypted_message = ''
    for i in message:
        if i == ' ':
            encrypted_message += i
        else:
            if i.isupper():
                encrypted_message += chr((ord(i) + shift - 64) % 26 + 65)
            else:
                encrypted_message +=  chr((ord(i) + shift - 96) % 26 + 97)
    return encrypted_message
        
test = "Hello la Plateforme"
print(test)
encrypted_message = caesar_encrypt(5,test)
print(encrypted_message)