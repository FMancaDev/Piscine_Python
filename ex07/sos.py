import sys

morse_code = {" ": "/", "A": ".-", "B": "-...", "C": "-.-.",
              "D": "-..", "E": ".", "F": "..-.", "H": "....",
              "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
              "M": "--", "N": "-.", "O": "---", "P": ".--.",
              "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
              "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
              "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---",
              "3": "...--", "4": "....-", "5": ".....", "6": "-....",
              "7": "--...", "8": "---..", "9": "----.", "0": "-----"}

def main():
    if len(sys.argv) > 2:
        print("AssertionError: the arguments are bad")
        exit()
    elif len(sys.argv) < 2:
        print("AssertionError: the arguments are bad")
        exit()

    for letters in sys.argv[1]:
        if letters.upper() not in morse_code:
            print("AssertionError: the arguments are bad")
            exit()

    print(' '.join([morse_code[letters.upper()] for letters in sys.argv[1]]))






if __name__ == "__main__":
    main()
