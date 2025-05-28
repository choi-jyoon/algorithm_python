n = int(input())
company = {}
people = []
for i in range(n):
    name, log = input().split()
    company[name] = log
    
for name, log in company.items():
    if log == 'enter':
        people.append(name)
   
people.sort(reverse=True)     
for p in people:
    print(p)