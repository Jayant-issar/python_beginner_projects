print('welcome to tip calculator')
total_bill = input('whats your total bill? \n')
tip = input('what percent of tip would you like to give? \n')
people_no = input('how many people to split the bill? \n')

bill_after_tip = float(total_bill)*(float(tip)/100)+float(total_bill)

each_bill = bill_after_tip/float(people_no)

print(each_bill)