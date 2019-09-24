import csv

def appender(row, word, n):
    global reviews
    
    if len(reviews) < n:
        if word in row[6]:
            reviews.append(row)

def counter(recommendation):
    global count
    
    if recommendation == "Recommended":
        count += 1

#hypothesis#
n = 1365
p = 0.15

h0 = "p = " + str(n*p)
h1 = "p != " + str(n*p)
############

reviews = []
word = "terrible"
count = 0

print("n = %i" %(n))
print("p = %.2f\n" %(p))
print("H0: %s" %(h0))
print("H1: %s\n" %(h1))

with open("steam_reviews.csv", encoding = "utf-8") as file:
    reader = csv.reader(file, delimiter = ";")
    reader = list(reader)
    reader.pop(0)

    list(map(lambda row: appender(row[0].split(","), word, n), reader))

list(map(lambda review: counter(review[5]), reviews))

print("%i/%i good reviews with '%s'!\n" %(count, n, word))

if count == n*p:
    print("H0 is not rejected.\n%s" %(h0))

else:
    print("H0 is rejected.\n%i != %.2f" %(count, n*p))
