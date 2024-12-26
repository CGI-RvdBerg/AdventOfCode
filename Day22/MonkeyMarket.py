with open('MonkeyMarket_Data.txt') as file:
    data = [int(line.strip()) for line in file]


def get_next_secret_number(secret_number):
    secret_number = ((secret_number*64) ^ secret_number) % 16777216
    secret_number = (int(secret_number/32) ^ secret_number) % 16777216
    secret_number = ((secret_number*2048) ^ secret_number) % 16777216
    return secret_number
final_nums = []
for number in data:
    for _ in range(2000):
        number = get_next_secret_number(number)
    final_nums.append(number)
print(final_nums)
print(sum(final_nums))