def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
    print_dict(count_letters(words))
    
def count_letters(strlist:list[str]) -> dict[str,int]:
    diction = {chr(c) : 0 for c in range(ord('a'),ord('z')+1)}
    for word in strlist:
        for char in word.lower():
            if (char >= 'a' and char <= 'z'):
                diction[char]+=1
    return diction

def print_dict(diction:dict[str,int])->None:
    for key in diction.keys():
        print(f'The character {key} occurred {diction[key]} times')
    return

if __name__ == '__main__':
    main()