def alphabet_position(letter):
    letter=letter.lower()
    return ord(letter) - 97

def rotate_character(char, rot):
    if char.isalpha() == False:
        return char #If its not an alphabet

    elif rot // 26 ==0:
        ans = alphabet_position(char) + rot

    else:
        rot = rot % 26
        ans = alphabet_position(char) + rot

    if ans // 26 <=0 :
        ans=ans

    else:
        ans=ans-26

    if char.islower():
        ans=ans+97
        return chr(ans)

    else:
        ans=ans+65
        return chr(ans)

def encrypt(text,rot):
    position = 0
    output_string = ""
    while(position < len(text)):
        newchar = rotate_character(text[position],rot)
        output_string = output_string + newchar
        position = position + 1
    return output_string
