def calculate_fibonacci_and_sum(step, num1, num2):
    # Validate input
    if step < 1:
        return "Undefined", ""
    
    fib = []
    for i in range(step + 2):  
        if i == 0:
            fib.append(num1)
        elif i == 1:
            fib.append(num2)
        else:
            fib.append(fib[i-1] + fib[i-2])
    
    sums = []
    left = 0
    right = len(fib) - 1
    
    while left < right:
        sums.append(fib[left] + fib[right])
        left += 1
        right -= 1
    if left == right:
        sums.append(fib[left])

    fib_str = " ".join(map(str, fib))
    sum_str = " ".join(map(str, sums))
    
    return fib_str, sum_str

def main():
    try:
        step = int(input())
        num1 = int(input())
        num2 = int(input())

        fibonacci, sums = calculate_fibonacci_and_sum(step, num1, num2)
        print(fibonacci)
        if fibonacci != "Undefined":
            print(sums)
            
    except ValueError:
        print("Undefined")

if __name__ == "__main__":
    main()