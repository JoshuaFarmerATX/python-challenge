import csv
import os
import pprint

states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

file_path = os.path.join("employee_data.csv")

with open(file_path, "r") as emp_file:
    csvreader = csv.reader(emp_file, delimiter = ",")
    file_header = next(csvreader)

    data = list(csvreader)
    data_list = []
    first_last = []
    bday_list = []
    soc_list = []

    for row in data:
        data_list.append(row)
    
    file_header.insert(2, "Last Name")
    file_header.pop(1)
    file_header.insert(1, "First Name")
    pprint.pprint(file_header)
    
    for i in range(len(data_list)):
        first_last = (data_list[i][1].split())
        data_list[i].insert(2, first_last[1])
        data_list[i].pop(1)
        data_list[i].insert(1, first_last[0])

    for bday in range(len(data_list)):
        bday_list = (data_list[bday][3].split("-"))
        data_list[bday].pop(3)
        data_list[bday].insert(3, f"{bday_list[1]}/{bday_list[2]}/{bday_list[0]}")

    for soc_num in range(len(data_list)):
        soc_list = (data_list[soc_num][4].split("-"))
        data_list[soc_num].pop(4)
        data_list[soc_num].insert(4, f"***-**-{soc_list[2]}")

    for state in range(len(data_list)):
        data_list[state].append(states[data_list[state][5]])
        data_list[state].pop(5)    

    pprint.pprint(data_list[0:5])

    out_file = os.path.join("NewFile.csv")
    
    with open(out_file, "w+", newline = "") as new_out:
        csv_writer = csv.writer(new_out, delimiter = ",")
        csv_writer.writerow(file_header)
        for rows in range(len(data_list)):
            csv_writer.writerow(data_list[rows])
        
        

