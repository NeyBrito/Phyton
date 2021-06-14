import emoji
from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(1.0)
print(emoji.emojize('BOOM BOOM POW :clock12:', use_aliases=True))
sleep(5.0)
