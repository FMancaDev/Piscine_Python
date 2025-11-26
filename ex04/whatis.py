# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fomanca <fomanca@student.42porto.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/25 16:54:30 by fomanca           #+#    #+#              #
#    Updated: 2025/11/26 15:32:12 by fomanca          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def is_int(number):
    if not number:
        return false
    if number[0] in ('-', '+'):
        return number[1:].isdigit()
    return number.isdigit()

if len(sys.argv) < 2:
    exit()

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    exit()

if not is_int(sys.argv[1]):
    print("AssertionError: argument is not an integer")
    exit()

if int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
