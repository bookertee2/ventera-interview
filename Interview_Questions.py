def iPrime(x):
    if(x==2):
        return True
    if(x>1):
        for i in range(2,x):
                if (x%i==0):
                    return False
                return True
    return False

def analyze(prices, price):
    total = 0
    prices = sorted(prices)
    index = 0
    for p in prices:
        total += prices
        if(p >= price):
            index = prices.index(p)
    mean = total/len(prices)
    center = len(prices) / 2
    median = 0
    if len(prices) % 2 == 0:
        median = sum(prices[center - 1:center + 1]) / 2.0
    else:
        median = prices[center]
    output = [mean,median,index]
    return output