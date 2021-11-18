# def testing():
# 	output = [val**2 for val in range(1,10) if val%2 == 0]
# 	print(output)

# if __name__ == "__main__":
# 	testing()

# lst = [1,2,3,4,5,6,7,8,9,0]
# opt = {value:lst[key]**3 for key, value in enumerate(lst) if value%2 != 0}
# print(opt

# lst = [1,2,3,4,5,6,7,8,9,0]
# output = {val:val**3 for val in lst if val%2 != 0}
# print(output)

# states = ['TN', 'KL', 'KA']
# capitals = ['Chennai', 'Trivandram', 'Bangalore']
# op = {st:cp for(st, cp) in zip(states, capitals)}
# print(op)

# lst = [1,2,2,3,4,5,6,7,8,9,0]
# op = {num for num in lst if num%2==0}
# print(op)

# generator comprehensions
# list = [1,2,3,4,5,6,7,8,9,0]
# opt = (opt**2 for opt in list if opt != 0)
# for i in opt:
# 	print(i)
