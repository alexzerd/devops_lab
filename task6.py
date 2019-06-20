
print("Input two sets")

n = set(map(int, input().split()))

m = set(map(int, input().split()))

diff = sorted(n.symmetric_difference(m))

print("Symmetric difference in ascending order:")

for i in range(len(diff)):
    print(diff[i])
