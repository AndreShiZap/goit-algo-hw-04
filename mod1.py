
from pathlib import Path
from colorama import Fore, Back, Style

# функція виводит імена всіх піддиректорій та файлів. 
# Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором. 
# Кольор директорії та файлів можливо задати. 
# Если не задано шляху фукція виводит зміст поточної директорії

def print_dir_content(current_dir = '.', shift=0, dir_colors=None, file_colors=None):
    try:
        current_dir = Path(current_dir)
        if dir_colors is None:
            dir_colors = Fore.YELLOW + Back.BLACK
        if file_colors is None:
            file_colors = Fore.CYAN + Back.BLACK
        for path in current_dir.iterdir():
            if path.is_dir():
                print(' ' * shift + dir_colors + f'- {path.name}' + Style.RESET_ALL)
                print_dir_content(path, shift + 2, dir_colors, file_colors)
            elif path.is_file():
                print(' ' * shift + file_colors + path.name + Style.RESET_ALL)
    except Exception as err:
        style = Fore.RED
        print(style + str(err) + Style.RESET_ALL)


def main():
    print_dir_content('C:/Users/Dell/Desktop/GoIT/Phyton/MyGame')

if __name__ == "__main__":
    main()
