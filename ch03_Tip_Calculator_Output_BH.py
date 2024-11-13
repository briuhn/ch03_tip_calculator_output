# Brian Herrera
# Tip Calculator Output
# 08/29/2024
# Creating a program that uses a for loop to calculate three options for tip.

def main():
    # ask for cost of meal store it as float
    cost = float(input("Enter the total of the meal cost: "))

    #tip percentages
    tipsPercentage = [.15, .20, .25]
    #use a for loop to go through percetages
    for x in tipsPercentage:
        #calcualte tip by multiplying the tips from cost
        tip =cost * x
        
        #calculate total by adding tip plus cost
        total = tip + cost

        #print
        print((x*100), "%")
        print("Tip Amount: ", round(tip,2))
        print("Total Amount: ", round(total,2))
        print()


if __name__ == "__main__":
    main()
