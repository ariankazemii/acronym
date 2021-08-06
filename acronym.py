def abbreviate(words):
    string_upper = words.upper()
    my_string = string_upper.replace('-',' ').replace('_',' ').split()
    abbreviation = []
    for letters in my_string :
        abbreviation.append(letters[0])

    answer = ''.join(abbreviation)

    return answer
    
