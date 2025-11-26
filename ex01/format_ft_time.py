# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fomanca <fomanca@student.42porto.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/23 18:27:38 by fomanca           #+#    #+#              #
#    Updated: 2025/11/25 15:32:03 by fomanca          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import time
from    datetime import datetime

seconds = time.time()

print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in  scientific notation")

now = datetime.now()
print(now.strftime("%b %d %Y"))
