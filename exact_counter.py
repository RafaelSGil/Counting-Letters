def exact_count(text, top=5):
    letter_count = {}
    
    for char in text:        
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
            
    sorted_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))

    return dict(list(sorted_count.items())[:top])