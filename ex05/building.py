# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fomanca <fomanca@student.42porto.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/26 16:50:10 by fomanca           #+#    #+#              #
#    Updated: 2025/11/26 17:25:50 by fomanca          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from string import punctuation

def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        exit();
    elif len(sys.argv) == 2:
        mensagem_count = sys.argv[1]
    else:
        print("What is the text to count?")
        mensagem_count = sys.stdin.readline()


    spaces = [' ', '\n']

    print(f"The text contains {len(mensagem_count)} characters:")
    print(f"{sum(1 for c in mensagem_count if c.isupper())} upper letters")
    print(f"{sum(1 for c in mensagem_count if c.islower())} lower letters")
    print(f"{sum(1 for c in mensagem_count if c in punctuation)} punctuation marks")
    print(f"{sum(1 for c in mensagem_count if c in spaces)} spaces")
    print(f"{sum(1 for c in mensagem_count if c.isdigit())} digits")



if __name__ == "__main__":
    main()
