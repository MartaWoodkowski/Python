import os
import csv

election_data_path = os.path.join("Resources", "election_data.csv")

Total_Votes = 0
Candidate_List = []
Votes_Per_Candidate = []
Percentage_Vote_Per_Candidate = []

#Extracting a list of unique names from the 'Candidate' column
def Unique_Candidate_List(names):

    Unique_Candidate_List = []

    Unique_Names = set(names)

    for name in Unique_Names:
        Unique_Candidate_List.append(name)

    return Unique_Candidate_List


with open(election_data_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csv_reader, None)
    
    for row in csv_reader:
        Total_Votes += 1
        Candidate_List.append(row[2])
       
    Candidates = Unique_Candidate_List(Candidate_List)
    
    for i in range(len(Candidates)):
        count = 0
        for j in range(len(Candidate_List)):
            if Candidates[i] == Candidate_List[j]:
                count += 1
         
        Votes_Per_Candidate.append(count)

    for x in range(len(Votes_Per_Candidate)):
        Percentage_Vote_Per_Candidate.append(Votes_Per_Candidate[x]/Total_Votes*100)
    
    Majority_Of_Votes = max (Votes_Per_Candidate)
    for z in range(len(Votes_Per_Candidate)):
        if Majority_Of_Votes == Votes_Per_Candidate[z]:
            Winner = Candidates[z]
    
    
    #Creating and Writing my budget_data_results.txt file in the analysis folder:
    output_path = os.path.join (".","analysis", "election_data_results.txt")
    w = open (output_path, "w")

    
    print("Election Results")
    w.write("Election Results\n") #writing (the same line I printed) to election_data_results.txt & moving to the next line
        
    print("-----------------------------")
    w.write("-----------------------------\n") #writing (the same line I printed) to election_data_results.txt & moving to the next line
        
    text = "Total Votes: " + str(Total_Votes)
    print(text)
    w.write(text+"\n") #writing (the same line I printed) to election_data_results.txt & moving to the next line
    
    print("-----------------------------")
    w.write("-----------------------------\n") #writing (the same line I printed) to election_data_results.txt & moving to the next line
    
    for y in range(len(Candidates)):
        text = Candidates[y] + ": " + f'{Percentage_Vote_Per_Candidate[y]:.3f}' + "% ("+ str(Votes_Per_Candidate[y]) +")"
        print(text)
        w.write(text+"\n") #writing (the same line I printed) to election_data_results.txt & moving to the next line
            
    print("-----------------------------")
    w.write("-----------------------------\n") #writing (the same line I printed) to election_data_results.txt & moving to the next line
    
    text = "Winner: " + Winner
    print(text)
    w.write(text+"\n") #writing (the same line I printed) to election_data_results.txt & moving to the next line
    
    print("-----------------------------")
    w.write("-----------------------------\n") #writing (the same line I printed) to election_data_results.txt & moving to the next line
    
    w.close() #stop writing to budget_data_results.txt