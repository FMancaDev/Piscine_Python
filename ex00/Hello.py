# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fomanca <fomanca@student.42porto.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/23 16:26:48 by fomanca           #+#    #+#              #
#    Updated: 2025/11/23 20:33:33 by fomanca          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import flake8

ft_list     = ["Hello", "tata!"]
ft_tuple     = ("Hello", "toto!")
ft_set      = {"Hello", "tutu!"}
ft_dict     = {"Hello" : "titi!"}

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "Portugal!")
ft_set = {"Hello!", "Porto!"}
ft_dict = {"Hello" : "42Porto"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
