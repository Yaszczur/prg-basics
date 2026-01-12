def f(x, y, digit):
    count = 0
    target = str(digit)
    
    for num in range(x, y + 1):
        count += str(num).count(target)
        
    return count

if __name__ == "__main__":
    print(f(10, 15, 1))    
    print(f(28, 32, 2)) 
    print(f(100, 105, 6)) 
    print(f(100, 101, 0))  