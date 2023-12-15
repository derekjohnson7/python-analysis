import os 
import csv

#create file path
budgetpath = os.path.join("election_data.csv")

#establish variables
candidate_name={}
CCS_votes = 0
DG_votes = 0
RAD_votes = 0
total_cast = []
    

#open and read the csv file
with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(budgetreader)

    #create a for loop to get the candidates name and add the total votes to the list
    for row in budgetreader:
        candidate_name = row[2]
        total_cast.append(row[0])

        #use if statement to match the number of votes cast to each candidate
        if candidate_name == "Charles Casper Stockham":
            CCS_votes += 1
        elif candidate_name == "Diana DeGette":
            DG_votes += 1
        elif candidate_name == 'Raymon Anthony Doane':
            RAD_votes +=1
           
        #find the total votes cast
        total_votes = CCS_votes + DG_votes + RAD_votes

        #find the percent of votes cast for each candidate
        CCS_pct = round((CCS_votes/total_votes) * 100,3)
        DG_pct = round((DG_votes/total_votes)* 100, 3)
        RAD_pct = round((RAD_votes/total_votes)*100,3)

    #determine the winner of the popular vote
    if CCS_pct > DG_pct and RAD_pct:
            win = "Charles Casper Stockham"
    elif DG_pct > RAD_pct:
            win = "Diana DeGette"
    else:
            win = "Raymon Anthony Doane"

        
#print the results
print("Election Results")
print('-------------------------')
print(f'Total Votes: {len(total_cast)}')   
print('-------------------------')
print('Charles Casper Stockham: '+ f'{CCS_pct}% ({CCS_votes})')
print('Diana DeGette: '+ f'{DG_pct}% ({DG_votes})')
print('Raymon Anthony Doane: '+ f'{RAD_pct}% ({RAD_votes})')
print('-------------------------')
print(f'Winner: {win}')

#create output path and write into it
output_path = os.path.join("analysis","analysis.txt")

with open(output_path, 'w') as txtfile:

    writer = csv.writer(txtfile)

    txtfile.write(("Election Results"))
    txtfile.write('\n''-------------------------')
    txtfile.write((f'\nTotal Votes: {len(total_cast)}'))
    txtfile.write(('\n''-------------------------'))
    txtfile.write(('\n''Charles Casper Stockham: '+ f'{CCS_pct}% ({CCS_votes})'))
    txtfile.write('\n''Diana DeGette: '+ f'{DG_pct}% ({DG_votes})')
    txtfile.write('\n''Raymon Anthony Doane: '+ f'{RAD_pct}% ({RAD_votes})')
    txtfile.write('\n''-------------------------')
    txtfile.write(f'\nWinner: {win}')