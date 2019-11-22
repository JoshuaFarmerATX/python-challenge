import csv
import os

file_path = os.path.join("budget_data.csv")

with open(file_path, "r") as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ",")
    file_header = next(csvreader)

    data = list(csvreader)

    months_count = 0
    net_total = 0
    last_month = 0
    this_month = 0
    month_OverUnder = 0
    OverUnder_list = []
    full_list = []

    for row in data:
        months_count += 1
        net_total += int(row[1])
        full_list.append(row)
 
    for i in range(0, months_count):
        if last_month == 0:
            last_month = full_list[i][1]
        else:
            this_month = full_list[i][1]
            month_OverUnder = int(this_month) - int(last_month)
            OverUnder_list.append(month_OverUnder)
            last_month = full_list[i][1]

    average_net = round(sum(OverUnder_list) / len(OverUnder_list), 2)
    min_OverUnder = min(OverUnder_list)
    min_index = OverUnder_list.index(min_OverUnder) + 1
    max_OverUnder = max(OverUnder_list)
    max_index = OverUnder_list.index(max_OverUnder) + 1
    max_increase = full_list[max_index][0]
    max_decrease = full_list[min_index][0]

    printout = f'''
    Financial Analysis
    ___________________________
    
    Total Months: {months_count}
    Total Net: ${net_total}
    Average Change: {average_net}
    Greatest Increase in Profit: {max_increase} (${max_OverUnder})
    Greatest Decrease in Profit: {max_decrease} (${min_OverUnder})
    '''
    print(printout)

    out_file = os.path.join("FinancialReport.txt")

    with open(out_file, "w+") as txt_out:
         
        txt_out.write(printout)
    