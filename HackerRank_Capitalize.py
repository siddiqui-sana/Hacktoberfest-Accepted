

# Solution of HackerRank problem, "Capitalize".
def solve(s):
    for x in s[:].split(): # Looping through the string in form of list.
        s = s.replace(x, x.capitalize()) #The replace function will replace the x with its capital form if x is alphanumeric otherwise, it would do nothing.
    return(s)

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

