import sys
from mod1 import print_dir_content

def main():
    path = sys.argv[1]
    print_dir_content(path)


if __name__ == "__main__":
    main()