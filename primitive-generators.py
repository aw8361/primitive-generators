import sys

def primitive_elements(n: int) -> list[int]:
    primitive_elements = []
    table = []
    for i in range(n - 1):
        table.insert(i, [])
        for j in range(n - 1):
            table[i].append(pow(i + 1, j + 1, n))
            if (table[i][j] == 1):
                if (j == n - 2):
                    primitive_elements.append(i + 1)
                else:
                    break
    return primitive_elements

if (len(sys.argv) != 2):
    print("Usage: primitive-generators.py [modulus]")
    sys.exit()
else:
    try:
        modulus = int(sys.argv[1])
    except:
        print("Usage: primitive-generators.py [modulus]")
        sys.exit()

elements = primitive_elements(modulus)
print(f"Number of elements: {len(elements)}")
print(f"Elements: {elements}")
