# Homework 6, happy1.py
#
# Eric Kye
#
# Create a function that creates a dictionary and assigns the country and
# happiness index value from a csv file we input


def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    # print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    # lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    #read_gdp_data(happy_dict)



def make_happy_dict():
    # open csv file
    infile=open('happiness.csv')
    # read and ignore first line
    infile.readline()
    # create a dict
    return_dict={}

    # loop through every line in the file
    for line in infile:
        # strip the "\n" line that is created from each line
        line=line.strip()

        # split each line by comma and put into a list
        codes=line.split(",")

        # create string variable for country and assign to first index of list
        country=codes[0]
        # create string variable for hap. index and assign to third index of list
        happiness=codes[2]
        
        # assign country to be the key and happiness index to be the value
        return_dict[country]=happiness
        
        print(country,happiness)
            
    
    return return_dict

def read_gdp_data(happy_dict):
    return

def lookup_happiness_by_country(happy_dict):
    return

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(D.keys()):
        print(key, D[key])
        
main()
