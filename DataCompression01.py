#!/usr/bin/env python3

# zlib supports several different compression levels, allowing a balance between computational
# cost and the amount of space reduction. The default compression level, zlib.Z_DEFAULT_COMPRESSION,
# is -1 and corresponds to a hard-coded value that represents a compromise between performance and
# compression outcome. This currently corresponds to level 6.

import zlib

input_data = b'CHANAKA LASANTHA CHANAKA LASANTHA CHANAKA LASANTHA CHANAKA LASANTHA CHANAKA LASANTHA CHANAKA LASANTHA CHANAKA LASANTHA CHANAKA LASANTHA CHANAKA LASANTHA .\n' * 1024
template = '{:>5} {:>5}'
print(template.format('Level', 'Size'))
print(template.format('-----', '----'))

for i in range(0, 10):
    data = zlib.compress(input_data, i)
    print(template.format(i, len(data)))
