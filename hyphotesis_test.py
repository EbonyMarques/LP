import csv

def reciever(row):
    global reviews
    
    if len(reviews) < n:
        if "nice" in row[6]:
            reviews.append(row)

def other_reciever(text):
    global count
    
    if text == "Not Recommended":
        count += 1

reviews = []
count = 0

n = 1365
p = 0.15

h0 = "p = " + str(n*p)
h1 = "p != " + str(n*p)

print("n = %i" %(n))
print("p = %f\n" %(p))

print("H0: %s" %(h0))
print("H1: %s\n" %(h1))

with open("steam_reviews.csv", encoding = "utf-8") as file:
    reader = csv.reader(file, delimiter = ";")
    reader = list(reader)
    reader.pop(0)

    list(map(lambda row: reciever(row[0].split(",")), reader))

list(map(lambda review: other_reciever(review[5]), reviews))

print("%i/%i bad reviews with 'nice'!\n" %(count, n))

if count == n*p:
    print("H0 is accepted.\n%s" %(h0))

else:
    print("H0 is rejected.\n%s" %(h1))
