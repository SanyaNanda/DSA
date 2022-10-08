import os

def reverse1(s):
    i=len(s)-1
    r=s[i]
    i=i-1
    while(i>=0):
        r+=s[i]
        i=i-1
    return r
        
def reverse2(s):
    return s[::-1]

if __name__ == '__main__':
    os.environ['OUTPUT_PATH']="/home/tapli/dsa/output.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #fptr = sys.stdout
    word = input()
    r = reverse1(word)
    fptr.write('Reverse from function 1: '+ str(r) + '\n')
    r1 = reverse2(word)
    fptr.write('Reverse from function 2: '+ str(r) + '\n')
    fptr.close()