def main():
    asdf = [ 1,2,3,4,5,6,7,8,9,10 ]
    i = 0
    while i < 10:
        i = g(i)
        print(i)
        i+=1
        
def g(i):
    return i+1
    
if __name__ == "__main__":
    main()
