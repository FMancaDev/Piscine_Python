# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fomanca <fomanca@student.42porto.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/25 15:34:28 by fomanca           #+#    #+#              #
#    Updated: 2025/11/25 16:52:19 by fomanca          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
    obj_type = object.__class__

    if object.__class__ == None.__class__:
        print(f"Nothing: {object} {obj_type}")
        return 0
    elif object.__class__ == float().__class__ and object != object:
        print(f"chesse: nan {obj_type}")
        return 0
    elif object.__class__ == int().__class__ and object == 0:
        print(f"Zero: {object} {obj_type}")
        return 0
    elif object.__class__ == str().__class__ and object == "":
        print(f"Empty: {object} {obj_type}")
        return 0
    elif object.__class__ == bool().__class__ and object is False:
        print(f"False: {object} {obj_type}")
        return 0
    else:
        print("Type not Found")
        return 1


if __name__ == "__main__":
    from NULL_not_found import NULL_not_found
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ""
    Fake = False
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))
