#HackerRank problem ,"Equal Stacks".

def equalStacks(h1, h2, h3):
    # Write your code here
    s1=0
    s2=0
    s3=0
    for i in h1:
        s1 += i
    for i in h2:
        s2 += i
    for i in h3:
        s3 += i
    while(1):
        if s1==0 or s2==0 or s3==0:
            return 0
        else:
            if (s1>=s2 and s1>s3)or(s1>s2 and s1>=s3):
                s1 -=h1[0]
                h1.pop(0)
            elif (s2>=s1 and s2>s3)or(s2>s1 and s2>=s3):
                s2 -= h2[0]
                h2.pop(0)
            elif (s3>=s1 and s3>s2)or(s3>s1 and s3>=s2):
                s3 -= h3[0]
                h3.pop(0)
            else:
                pass
            if s1==s2==s3:
                return s1
                
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)
