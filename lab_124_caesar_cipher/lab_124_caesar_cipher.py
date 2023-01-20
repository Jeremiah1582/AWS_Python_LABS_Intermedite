# user Defined function- function attached to modules that the user has made 
def getDoubleAlphabet(alphabet):
    doubleAlphabet= alphabet + alphabet
    return doubleAlphabet

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = input("please enter a key ( whole number from 1-15) ")
    return shiftAmount



def encryptMsg(msg, cipherKey, alphabet):
    print("this is msg type()...", type(msg))
    print("Msg is ... ",msg)
    
    encryptedMsg =""
    # uppercaseMsg= ""
    testString= str(msg)
    uppercaseMsg= testString.upper()
    
    
    for letter in uppercaseMsg:
        position = alphabet.find(letter)
        newPosition= position + int(cipherKey)
        if letter in alphabet:
            encryptedMsg = encryptedMsg + alphabet[newPosition]
        else:
            encryptedMsg = encryptedMsg + letter
            
    return encryptedMsg # <---problem was here: be careful not to give Variable names that are too similar  

def decryptMsg(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMsg(message, decryptKey, alphabet)

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    
    myEncryptedMessage = encryptMsg(myMessage, myCipherKey, myAlphabet2)
    print("myMessage is ...", myMessage)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMsg(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
runCaesarCipherProgram()