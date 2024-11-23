from ultimate import Gates
print("Logic Gates true results:")

a = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
b = [0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1]
c = [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1]
d = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]

a_and_b = []

c_or_d = []

b_and_c = []
b_and_c_and_d = []

a_and_b_or_c_or_d = []
not_a_and_b_or_c_or_d = []

x = [] # The final answer

# A * B
for i in range(len(a)):
    a_and_b.append(Gates.land(a[i], b[i]))

# C + D
for i in range(len(a)):
    c_or_d.append(Gates.lor(c[i], d[i]))

# B * C * D
for i in range(len(a)):
    b_and_c.append(Gates.land(b[i], c[i]))
else:
    for i in range(len(a)):
        b_and_c_and_d.append(Gates.land(b_and_c[i], d[i]))

# (A * B) + (C + D)
for i in range(len(a)):
    a_and_b_or_c_or_d.append(Gates.lor(a_and_b[i], c_or_d[i]))

# ~((A * B) + (C + D))
for i in range(len(a)):
    not_a_and_b_or_c_or_d.append(Gates.lnot(a_and_b_or_c_or_d[i]))

# (~((A * B) + (C + D))) * (B * C * D)
for i in range(len(a)):
    x.append(Gates.land(not_a_and_b_or_c_or_d[i], b_and_c_and_d[i]))

print("A     B     C     D   A*B   C+D   B*C*D   (A*B)+(C+D)   ~((A*B)+(C+D))   (~((A*B)+(C+D)))*(B*C*D)")
for i in range(len(a)):
    print(f"{a[i]}     {b[i]}     {c[i]}     {d[i]}    {a_and_b[i]}     {c_or_d[i]}      {b_and_c_and_d[i]}          {a_and_b_or_c_or_d[i]}               {not_a_and_b_or_c_or_d[i]}                    {x[i]}")
