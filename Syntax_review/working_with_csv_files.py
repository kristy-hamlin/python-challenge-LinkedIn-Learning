# To work with CSV files, you need to include the import statement:
import csv

# --------------------- READING CSV FILES --------------------

# To open a CSV file, we open it using the same method as we used for a text file.
# However, once we have the file object, we need to pass that to a csv reader:

def csvReadingDemo1():
    with open('boxoffice_data_2024.csv', 'r') as f:
        # NOTE: If your csv file uses anything other than a comma for a delimiter, you
        # pass that in as a keyword argument for 'delimiter=x' for it to parse correctly. 
        reader = csv.reader(f)
        # If we print the type(reader), we will see that it is a csv.reader object.
        # However, it is an iterable object, and we can iterate over it to print
        # every row if we want to:
        for row in reader:
            print(row)

def csvReadingDemo2():
    # Another common way to work with csv files is to convert the reader directly to a list.
    # Once it is a list, we can use our splicing syntax to look at any row we want:
    with open('boxoffice_data_2024.csv', 'r') as f:
        reader = list(csv.reader(f))
        print(reader[0])
        # Notice that the first row of this CSV file, like many CSV files, is actually headers.
        # ['Year', 'Title', 'Gross']
        # We will use that next. 

def csvReadingDemo3():
    # Another option is to use a DictReader() which uses the first row and creates a list of
    # dictionaries, where the headers are the key values for each of the inner dictionaries.
    # This can be very convenient to work with:
    with open('boxoffice_data_2024.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

def csvReadingDemo4():
    # Instead of using the DictReader object, we can also convert that to a regular old
    # list of dictionaries. One common syntax is to simply call that list 'data':
    with open('boxoffice_data_2024.csv', 'r') as f:
        data = list(csv.DictReader(f))
        for row in data:
            print(row)


# ------------------ FILTERING DATA ----------------------
def csvFilteringDemo1():
    # We can use list comprehensions and our dictionary accessing syntax
    # to create a dictionary of only the values that interest us or that
    # meet some criteria:
    with open('boxoffice_data_2024.csv', 'r') as f:
        data = list(csv.DictReader(f))
        print(len(data))
        data2 = [row for row in data if int(row['Gross'].replace('$', '').replace(',', '')) > 10000000]
        print(len(data2))
    # By the way, recall that we have converted data into a regular old list.
    # Therefore, that list will still be available and editable outside of the 
    # with open() block, when the file object is closed. 

# ------------------ WRITING CSV FILES ---------------------
def csvWritingDemo1():
    # Writing a csv file is similar to writing a text file. You open
    # the file in 'w' mode, and it will create or overwrite the file:
    # To write a new csv file, we will first get and filter data similar to
    # above:
    with open('boxoffice_data_2024.csv', 'r') as r:
        data = list(csv.DictReader(r))
        data2 = [row for row in data if (row['Title'][0] == 'K')]

    with open('K_movies.csv', 'w') as f:
        writer = csv.writer(f)
        for row in data2:
            writer.writerow([row['Title'], row['Gross'], row['Year']])

csvWritingDemo1()

# End of CSV Lesson

