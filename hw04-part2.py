from pathlib import Path
from pprint import pprint

# функція аналізує файл "cats.txt" і повертає 
# список словників з інформацією про кожного кота.
# файл "cats.txt"  має бути у той же діректорії, де є файл, що виконується
def get_cats_info(path):
    file_path = Path(path)
    result = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                dict_cat = {}
                id, name, age = line.split(',')
                age = int(age.rstrip('\n'))
                dict_cat = {'id': id, 'name': name, 'age': age}
                result.append(dict_cat)
        return(result)
    except:
        print(f"{file_path} does not exist or is not a file")
    return result


def main():
    pprint(get_cats_info('cats.txt'))
    


if __name__ == "__main__":
    main()
