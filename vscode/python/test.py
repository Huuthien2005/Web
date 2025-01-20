#x=int(input("nhập vào một số ngẫu nhiên"))
def factory(n):
    if n==0:
        return 1
    else:
        return n*factory(n-1)
def sum_fact(m):
    if m==1:
        return 1
    else:
        return factory(m)+ sum_fact(m-1)
def power(x,y):
    if y==0:
        return 1
    else:
        return x*power(x,y-1)
list={4,3,6,1,2,7,6,8,9}
def bubble_sort(x,y):
    for i in list.length():
        for j in range(y):
            list[j]=list[j+1]

def main():
    print("ham main duoc chay")
if __name__== "__main__":
    main()
    #print(sum_fact(x))
    print(power(2,4))

