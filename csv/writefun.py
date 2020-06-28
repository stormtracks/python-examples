import csv

def read_test():
    with open('ui-fun.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

def write_csv1(index,symbol,dyield,payout):
    with open('eggs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(['index'] + ['symbol'] + ['yield'] + ['payout'])
        spamwriter.writerow([index,symbol,dyield,payout])

def write_test_1():
    c1 = "1"
    c2 = "ui"
    c3 = "1.1"
    c4 = "10%"
    write_csv1(c1,c2,c3,c4)

if __name__ == "__main__":
    write_test_1()
