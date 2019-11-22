import csv
import os
import pprint

file_path = os.path.join("election_data.csv")

with open(file_path, "r") as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ",")
    file_header = next(file_reader)

    data = list(file_reader)

    total_votes = 0
    candidate_vote_percent = 0
    candidates_list = []
    candidates_vote = 0
    candidates_vote_list = []
    total_candidates = 0
    data_list = []
    candidates_dict = {}
    sorted_list = []
    

    for row in data:
        total_votes += 1
        data_list.append(row)
        
    for item in range(0, total_votes):
        if item == 0:
            candidates_list.append(data_list[item][2])
        elif data_list[item][2] not in candidates_list:
            candidates_list.append(data_list[item][2])
        else:
            continue

    for n in range(len(candidates_list)):
        for i in range(total_votes):
            if candidates_list[n] in data_list[i][2]:
                candidates_vote += 1
        candidates_vote_list.append(candidates_vote)
        candidates_vote = 0

    for names in range(len(candidates_list)):
        candidates_dict.update({candidates_vote_list[names]: candidates_list[names]})


    sorted_list = sorted(candidates_vote_list, reverse = True)

    out_file = os.path.join("Voting_Results.txt")
    with open(out_file, "w+") as txt_out:
        txt_out.write(f'''
Election Results
-------------------------
Total Votes = {total_votes}
-------------------------''')

        for name in sorted_list:
            txt_out.write(f'''
{candidates_dict[name]}: {round((name / total_votes) * 100)}% ({name})''')
        
        txt_out.write(f'''
-------------------------
Winner: {candidates_dict[sorted_list[0]]}''')
    with open(out_file, "r") as txt_read:
        print(txt_read.read())




