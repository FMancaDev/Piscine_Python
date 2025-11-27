import sys
from ft_filter import ft_filter

def main():
    if len(sys.argv) > 3:
        print("AssertionError: the arguments are bad")
        exit()
    elif len(sys.argv) < 3:
        print("AssertionError: the arguments are bad")
        exit()

    if not sys.argv[2].isdigit():
        print("AssertionError: the arguments are bad")
        exit()

    words = sys.argv[1].split(' ')
    size = int(sys.argv[2])
    print(list(ft_filter(lambda x: len(x) > size, words)))

if __name__ == "__main__":
    main()
