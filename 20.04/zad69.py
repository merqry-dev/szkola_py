from collections import Counter

f = open("20.04\\dane_geny.txt", "r")
arr = f.read().splitlines()
f.close()

# a
gt_arr = []
for i in arr:
    gt_arr.append(len(i))

num_of_gt = Counter(gt_arr)

# b / c
gens = []
n_of_gen = []
n = 0
for i in arr:
    start = 0
    end = 0
    gens.append("sep")
    x = i
    for j in range(len(i)):
        if "AA" in x:
            start = x.index("AA")
            if "BB" in x[start:]:
                end = x.index("BB", start)
                gens.append(x[start:end + 2])
                n += 1
                x = x[end + 2:]
    n_of_gen.append(n)
    n = 0


for i in gens:
    if "BCDDC" in i:
        n += 1

# d
n_o = 0
n_so = 0
temp = gens
for i in arr:

    if i == i[::-1]:
        n_so += 1

gens_inv = []
arr_inv = []
for i in arr:
    arr_inv.append(i[::-1])

for i in arr_inv:
    start = 0
    end = 0
    x = i
    gens_inv.append("sep")
    for j in range(len(i)):
        if "AA" in x:
            start = x.index("AA")
            if "BB" in x[start:]:
                end = x.index("BB", start)
                gens_inv.append(x[start:end + 2])
                x = x[end + 2:]


tmp = "".join(gens)
tmp_inv = "".join(gens_inv)

tmp2 = []
tmp_inv2 = []

tmp2 = tmp.split("sep")
tmp_inv2 = tmp_inv.split("sep")

if tmp[0] == 's':
    n_o += 1

if tmp_inv[0] == 's':
    n_o += 1


for i in range(len(tmp2)):
    if tmp2[i] == tmp_inv2[i]:
        n_o += 1

f = open("20.04\\wynik.txt", "w")
# a
f.write("a:\n")
f.write(str(len(num_of_gt)) + '\n')
f.write(str(num_of_gt.most_common(1)[0][1]) + '\n')

# b
f.write("b:\n")
f.write(str(n) + '\n')

# c
f.write("c:\n")
f.write(str(max(n_of_gen)) + "\n")
f.write(str(len(max(gens, key=len))) + '\n')

# d
f.write("d:\n")
f.write(str(n_o) + "\n")
f.write(str(n_so) + "\n")
f.close()
