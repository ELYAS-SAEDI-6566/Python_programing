def reverse(text = str):
    words_list = text.split()
    words_list.reverse()
    text = words_list[0]
    for word in words_list[1:]:
        text += " " + word
    return text