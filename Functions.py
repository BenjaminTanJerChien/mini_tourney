import csv
from os.path import exists



#csv file functions 
def check_csv(target):
        return exists(target)

def create_csv(csv_name):
    if csv_name == "rego":
        target = "rego.csv"
        if check_csv(target) == True:
            data = read_csv(target)
            return "CSV file 'rego' is here"
        else:
            header = ["Name", "Institution", "Team Name", "Contact Number", "Break Eligibility "]
            write_csv(target, header)
            return "CSV file 'rego' created"
    if csv_name ==

def read_csv(target_file):
    with open (target_file, 'r') as file:
            read = csv.reader(file)
            content = []
            for row in read:
                content.append(row)
    return content

def write_csv(target_file, towrite):
    with open (target_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(towrite)
    return


def add_team(format):
    team_name = input("Team Name: ")
    



if __name__ == "__main__":
    print(create_csv("rego"))