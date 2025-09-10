t = int(input())
for _ in range(t):
    n = int(input())
    funds = list(map(int, input().split()))
    
    ### 날마다 주식 살/말 정해서 최대 이익 남기기 
    sell = funds[-1]
    buy = []
    benefit = 0
    
    for fund in funds[-2::-1]:
        if fund < sell:
            benefit += sell - fund
        else:
            sell = fund 
        # print(fund, sell, buy, benefit)
    print(benefit)
    