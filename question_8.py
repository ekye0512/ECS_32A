while True:
    filename = input("Enter filename:")
    try:
        infile = open(filename)
        break
    except:
        continue
    
infile.close()
