# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fomanca <fomanca@student.42porto.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/23 20:48:05 by fomanca           #+#    #+#              #
#    Updated: 2025/11/25 15:29:17 by fomanca          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
    obj_type = object.__class__

    if object.__class__ == list().__class__:
        print(f"List : {obj_type}")
    elif object.__class__ == tuple().__class__:
        print(f"Tuple : {obj_type}")
    elif object.__class__ == set().__class__:
        print(f"Set : {obj_type}")
    elif object.__class__ == dict().__class__:
        print(f"Dict : {obj_type}")
    elif object.__class__ == str().__class__:
        print(
            f"{object} is in the kitchen : "
            f"{obj_type}"
        )
    else:
        print("Type not found")
    return 42
