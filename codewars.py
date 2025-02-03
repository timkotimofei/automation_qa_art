from operator import index


def one_down(txt):
    try:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        list_txt_from_alphabet = [alphabet.index(i) if i in alphabet else i for i in txt ]
        answer_txt = ''
        for items in list_txt_from_alphabet:
            if items != ' ':
                answer_txt += alphabet[items-1:items:]
            else:
                answer_txt += items
        return answer_txt
    except TypeError:
        return "Input is not a string"


print(one_down("CodeWars RockZ"))
