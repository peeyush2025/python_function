def decimal_to_binary(n):
    if n==0:
        return"0"
    binary_representation=""
    for i in range(n.bit_length()-1,-1,-1):
        binary_digit=0
        for j in range(i,i+1):
            if n>=(1<<j):
                n-= (1 << j)
                binary_digit=1
        binary_representation+=str(binary_digit)
    return binary_representation  
num=13
binary=decimal_to_binary(num)
print(f"the binary representation of{num}is{binary}")
