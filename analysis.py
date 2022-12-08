import statistics 
import csv 
import statistics
import matplotlib.pyplot as plt

aapl_data = []
msft_data = []
abnb_data = []
cvs_data = []        

empty_list = [aapl_data,msft_data,abnb_data,cvs_data]
files = ["AAPL.csv","MSFT.csv","ABNB.csv","CVS.csv"]
stock_dict = dict(zip(files,empty_list))

for name in files:
    with open("stocks_folder/"+name,"r") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            stock_dict[name].append(row)

def week_stdev(prop_name,lst):
    i = 0
    standard_dev = []
    dates = []
    while i < len(lst):
        try:
            month = []
            for j in range(21):
                day = float(lst[i+j]["Closing_Price"])
                month.append(day)
            standard_dev.append(statistics.pstdev(month))
            i += 21
        except:
            break   
        
    plt.plot(standard_dev)
    plt.title(f"{prop_name} 2021-2022 Monthly Standard Deviations")
    plt.xlabel("Dates",fontsize = 10)
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7,8,9,10,11], ["2021-04","2021-05","2021-06","2021-07","2021-08","2021-09","2021-10","2021-11","2021-12","2022-01","2022-02","2022-03"])
    plt.tight_layout()
    plt.ylabel("STDEV of Closing Price")

    plt.show()

for name,data in stock_dict.items():
    prop_name = name.split(".")[0]
    week_stdev(prop_name,data)
