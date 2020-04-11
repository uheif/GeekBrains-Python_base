import json

profit_sum = 0
cnt = 0
firms_dict = {}
with open("5.7.txt") as inf:
    for line in inf:
        firm_profit = int(line.split()[-2]) - int(line.split()[-1])
        if firm_profit > 0:
            profit_sum += firm_profit
        firms_dict[line.split()[0]] = firm_profit
        cnt += 1

firms_list = [firms_dict, {"average_profit": int(profit_sum / cnt)}]

with open("5.7_json.json", 'w') as ouf:
    json.dump(firms_list, ouf)
