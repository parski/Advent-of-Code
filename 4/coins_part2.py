import md5

def six_leading_zeroes_in_hash(hash):
    for digit in hash[:6]:
        if digit != '0':
            return False
    return True

def hex_md5(seed):
    return md5.new(seed).hexdigest()

seed = 'yzbqklnj'
iteration = 0
hash = hex_md5(seed + str(iteration))

while six_leading_zeroes_in_hash(hash) == False:
    iteration += 1
    hash = hex_md5(seed + str(iteration))

print(iteration)

