import os 
import csv

budgetpath = os.path.join("election_data.csv")

candidate_name={"Charles Casper Stockham", "Diana DeGette", 'Raymon Anthony Doane'}
CCS_votes = 0
DG_votes = 0
RAD_votes = 0
total_cast = []
    


with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(budgetreader)

    for row in budgetreader:
        candidate_name = row[2]
        total_cast.append(row[0])

        if candidate_name == "Charles Casper Stockham":
            CCS_votes += 1
        elif candidate_name == "Diana DeGette":
            DG_votes += 1
        elif candidate_name == 'Raymon Anthony Doane':
            RAD_votes +=1
           

        total_votes = CCS_votes + DG_votes + RAD_votes

        CCS_pct = round((CCS_votes/total_votes) * 100,3)
        DG_pct = round((DG_votes/total_votes)* 100, 3)
        RAD_pct = round((RAD_votes/total_votes)*100,3)

    if CCS_pct > DG_pct and RAD_pct:
            win = "Charles Casper Stockham"
    elif DG_pct > RAD_pct:
            win = "Diana DeGette"
    else:
            win = "Raymon Anthony Doane"

        

print("Election Results")
print('-------------------------')
print(f'Total Votes: {len(total_cast)}')   
print('-------------------------')
print('Charles Casper Stockham: '+ f'{CCS_pct}% ({CCS_votes})')
print('Diana DeGette: '+ f'{DG_pct}% ({DG_votes})')
print('Raymon Anthony Doane: '+ f'{DG_pct}% ({DG_votes})')
print('-------------------------')
print(f'Winner: {win}: {max(CCS_pct, DG_pct,RAD_pct)}%')

output_path = os.path.join("analysis","analysis.txt")

with open(output_path, 'w') as txtfile:

    writer = csv.writer(txtfile)

    txtfile.write(("Election Results"))
    txtfile.write('\n''-------------------------')
    txtfile.write((f'\nTotal Votes: {len(total_cast)}'))
    txtfile.write(('\n''-------------------------'))
    txtfile.write(('\n''Charles Casper Stockham: '+ f'{CCS_pct}% ({CCS_votes})'))
    txtfile.write('\n''Diana DeGette: '+ f'{DG_pct}% ({DG_votes})')
    txtfile.write('\n''Raymon Anthony Doane: '+ f'{DG_pct}% ({DG_votes})')
    txtfile.write('\n''-------------------------')
    txtfile.write(f'\nWinner: {win}: {max(CCS_pct, DG_pct,RAD_pct)}%')