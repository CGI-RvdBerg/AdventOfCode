from collections import defaultdict

with open('MonkeyMarket_Data.txt') as file:
    data = [int(line.strip()) for line in file]


def get_next_secret_number(secret_number):
    secret_number = ((secret_number*64) ^ secret_number) % 16777216
    secret_number = (int(secret_number/32) ^ secret_number) % 16777216
    secret_number = ((secret_number*2048) ^ secret_number) % 16777216
    return secret_number

sequence_prices = defaultdict(int)
for number in data:
    prices = []
    diffs = []
    for _ in range(2000):
        price = number % 10
        try:
         diff = price - prices[-1]
        except IndexError:
            diff = None
        prices.append(price)
        diffs.append(diff)
        number = get_next_secret_number(number)
    sequences = set()
    info_dict = defaultdict(int)
    for i in range(4,len(prices)):
        sequence = tuple(diffs[i-3:i+1])
        if sequence not in sequences:
            sequences.add(sequence)
            sequence_prices[sequence] += prices[i]
print(max(sequence_prices.values()))