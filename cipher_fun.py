#PROGRESSIVE CEASAR CIPHER TEST

def encrypt(plain_text, shift):
    # Ensure that only strings will be processed for the plain_text
    plain_text = str(plain_text)

    # Ensure that only integer will be processed for the shift variable
    # also initialize the the shift value
    shift = int(shift)

    # Empty string to serve as container for the concatenated letters per iteration
    coded_text = ""

    for letter in plain_text:
        # re-definine the caesar_cipher in every iteration (each letter)
        # define the allowed characters in a password as well as it's position in the cipher using tuple
        characters_array = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]","|","\\",":",";","\"","'","<",">",",",".","?","/"," ","\t")

        #Initialize `caesar_cipher` as dictionary list
        caesar_cipher = dict()

        c_array_size = len(characters_array) #define the array size of the tuple = 94
        for c in range(c_array_size):
            # c+shift = compute for the encryption offset (caesar function) of a character within the tuple
            # use modulo `%` to perform a loopback to handle when c+shift is > 94
            # [(70+10) % 94] = 80 => {'*':']'}
            # [(90+10) % 94] = 6 => {'.':'F'}
            caesar_cipher.update({characters_array[c]:characters_array[(c+shift) % c_array_size]})
                    
        for k, v in caesar_cipher.items():
            if letter == k:
                coded_text =  coded_text + v
                shift += 1 # increment the shift in each interation   

    return coded_text

def decrypt(plain_text, shift):
    # Ensure that only strings will be processed for the plain_text
    plain_text = str(plain_text)

    # Ensure that only integer will be processed for the shift variable
    shift = int(shift)

    # Empty string to serve as container for the concatenated letters per iteration
    coded_text = ""    

    for letter in plain_text:
        #perform re-difinition in every iteration
        #define the allowed characters in a password as well as it's position in the cipher using tuple
        characters_array = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]","|","\\",":",";","\"","'","<",">",",",".","?","/"," ","\t")
        #Initialize `caesar_cipher` as dictionary list
        caesar_cipher = dict()

        c_array_size = len(characters_array) #define the array size of the tuple = 94
        for c in range(c_array_size):
            # c-shift = compute for the decryption offset (caesar function) of a character within the tuple
            # use modulo `%` to perform a loopback to handle c-shift is < 0, or is a negative value
            # [(18-10) % 94] = 8 => {'R':'H'}
            # [(8-10) % 94] = 92 => {'H':'/'}
            caesar_cipher.update({characters_array[c]:characters_array[(c-shift) % c_array_size]})

        for k, v in caesar_cipher.items():
            if letter == k:
                coded_text =  coded_text + v
                shift += 1

    return coded_text


# testing:
offset = 10 # fixed offset

test = "hell0_  world?!123 .%l33t"
# line 75 below to test a variable offset based on the string length
offset = len(test)

print(f"\nPlain-text: {test} \n")

encrypted_test = encrypt(test, offset)
print(f"Encrypted: {encrypted_test} \n")

decrypted_test = decrypt(encrypted_test, offset)
print(f"Decrypted: {decrypted_test} \n")

# testing parity
print(f"Is Parity confirmed? Response: {test == decrypted_test}")