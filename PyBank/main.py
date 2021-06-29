import os
import csv

budget_data_path = os.path.join(".","Resources", "budget_data.csv")

Total_Months = 0
Total_Amount = 0
Profit_Loss_Data = []
Profit_Loss_Change = []
Date_Recorded = []

with open(budget_data_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csv_reader, None)
    
    for row in csv_reader:
        Total_Months += 1
        Total_Amount += int(row[1])
        Profit_Loss_Data.append(int(row[1]))
        Date_Recorded.append(row[0])
         
    for i in range(len(Profit_Loss_Data)-1):
        Profit_Loss_Change.append(Profit_Loss_Data[i+1]-Profit_Loss_Data[i])
    Average_Change = sum(Profit_Loss_Change)/len(Profit_Loss_Change)
  
    Greatest_Increase = max(Profit_Loss_Change)
    for i in range(len(Profit_Loss_Change)):
        if Greatest_Increase == Profit_Loss_Change [i]:
            Greatest_Increase_Date = Date_Recorded[i+1]
    
    Greatest_Decrease = min(Profit_Loss_Change)
    for i in range(len(Profit_Loss_Change)):
        if Greatest_Decrease == Profit_Loss_Change [i]:
            Greatest_Decrease_Date = Date_Recorded[i+1]
    
    
    #Creating and Writing my budget_data_results.txt file in the analysis folder:
    output_path = os.path.join (".","analysis", "budget_data_results.txt")
    w = open (output_path, "w")

    print("Financial Analysis")
    w.write("Financial Analysis\n") #writing (the same line I printed) to budget_data_results.txt & moving to the next line
    
    print("--------------------------------------------------")
    w.write("--------------------------------------------------\n") #writing (the same line I printed) to budget_data_results.txt & moving to the next line
    
    text = "Total Months: "+str(Total_Months)
    print(text)
    w.write(text+"\n") #writing (the same line I printed) to budget_data_results.txt  & moving to the next line
            
    text = "Total: $" + str(Total_Amount)
    print(text)
    w.write(text+"\n") #writing (the same line I printed) to budget_data_results.txt  & moving to the next line
    
    text = "Average Change: $" + str(round(Average_Change,2))
    print(text)
    w.write(text+"\n") #writing (the same line I printed) to budget_data_results.txt  & moving to the next line
    
    text = "Greatest Increase in Profits: " + Greatest_Increase_Date + " ($"+ str(Greatest_Increase)+")"
    print(text)
    w.write(text+"\n") #writing (the same line I printed) to budget_data_results.txt & moving to the next line
    
    text = "Greatest Decrease in Profits: " + Greatest_Decrease_Date + " ($"+ str(Greatest_Decrease)+")"
    print(text)
    w.write(text) #writing (the same line I printed) to budget_data_results.txt 
   
    w.close() #stop writing to budget_data_results.txt
