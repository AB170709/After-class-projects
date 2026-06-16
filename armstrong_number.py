num= int(input("Enter a number: "))
if num<0:
    print("Armstrong numbers are defined only for non-negative integers.")
else:
    original_num=num
    if num==0:
        num_of_digits=1
    else:
        num_of_digits=0
        temp=num
        while temp>0:
            temp=temp//10
            num_of_digits+=1
    sum_of_powers=0
    temp=original_num
    while temp>0:
        digit=temp%10
        sum_of_powers+=digit**num_of_digits
        temp = temp//10
    if sum_of_powers == original_num:
        print(f"{original_num} is an Armstrong number.")
    else:
        print(f"{original_num} is NOT an Armstrong number.")