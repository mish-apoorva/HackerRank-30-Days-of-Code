# Enter your code here. Read input from STDIN. Print output to STDOUT

returned_date = list(map(int,input().split(' ')))
expected_date = list(map(int,input().split(' ')))

fine = 0

if returned_date[2] > expected_date[2]:
    fine = 10000
elif returned_date[2] == expected_date[2]:
    if returned_date[1] > expected_date[1]:
        fine = (returned_date[1] - expected_date[1])*500
    elif returned_date[1] == expected_date[1]:
        if returned_date[0] > expected_date[0]:
            fine = (returned_date[0] - expected_date[0])*15
    
print(fine)

