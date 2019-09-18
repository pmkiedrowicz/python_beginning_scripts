'''
Generate 6 digit random secure OTP
'''

import secrets

generator = secrets.SystemRandom()
random_num = generator.randint(100000, 999999)
print(random_num)
