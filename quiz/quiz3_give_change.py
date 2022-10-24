def give_change(dollars):
    cents = int(dollars * 100)
    change = []
    coins = [200, 100, 50, 25, 10, 5]
    
    for i in range(len(coins)):
        change.append(cents // coins[i])
        cents = cents % coins[i]
        
    return change
        