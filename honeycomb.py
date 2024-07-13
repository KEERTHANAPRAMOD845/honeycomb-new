def print_hexagon_shell():
    print(" ___ ")
    print("/   \\")
    print("\\___/")

def print_honeycomb(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(" ___ ", end="")
        print()
        for j in range(cols):
            print("/   \\", end="")
        print()
        for j in range(cols):
            print("\\___/", end="")
        print()

rows = int(input("Enter the rows: "))
cols = int(input("Enter the cols: "))
print_honeycomb(rows, cols)
