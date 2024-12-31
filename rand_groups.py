import random

dev_li = [
    "Noor",
    "Brady",
    "Dylan",
    "Sharala",
    "Lawrence",
    "Scott",
    #"Aman",
    "Sarah",
    "Anthony",
    "Milos"
]

num_devs = len(dev_li)
num_groups = 2
group_size = num_devs // num_groups

random.shuffle(dev_li)
rand_groups = [dev_li[i * group_size:(i + 1) * group_size] for i in range((num_devs + group_size - 1) // group_size )]

if group_size * num_groups != num_devs:
    rand_group = random.randrange(0,num_groups)
    rand_groups[rand_group].append(rand_groups[-1][0])
    rand_groups.pop(-1)

count = 0
for group in rand_groups: 
    print("Group ", count + 1, ": ")
    print(rand_groups[count])
    count = count + 1
