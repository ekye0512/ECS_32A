# Homework 6, happy2.py
#
# Eric Kye
#
# Simply to test out if the dictionary that I created works and is properly sorted



def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    # lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    #read_gdp_data(happy_dict)



def make_happy_dict():
    infile=open('happiness.csv')
    infile.readline()
    return_dict={}
    
    for line in infile:
        line=line.strip()
        
        
        
        codes=line.split(",")

     
        country=codes[0]
        happiness=codes[2]

        return_dict[country]=happiness
        #print(country,happiness)
            
    
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
