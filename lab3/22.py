def solve(numheads, numlegs):
    if numlegs % 2 == 1:
        print("Error")
        return None
    if numheads > (numlegs / 2):
        print("Error")
        return None
    

x = int(input("Write number of heads\n"))
y = int(input("Write number of legs\n"))
solve(x, y)
b = int(y/2 - x)
a = int(x - b)
print("The number of chickens: ", a)
print("The number of rabbit: ", b)
