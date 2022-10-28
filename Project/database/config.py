from configparser import ConfigParser 


def config(filename="database.ini", section="postgresql"):
    # create a parser 
    parser = ConfigParser()
    # Read config file 
    parser.read(filename)
    # Iterate through the filename and return each element inside the file and put it in a dictnioary
    # Create empty dictionary
    db = {}
    # condition to check if the ini file has the section defined
    if parser.has_section(section):
        # If so, extract the elements on the script tuple format
        params = parser.items(section)
        # Loop through each param and add elements to dictionary
        for param in params:
            db[param[0]] = param[1]
    else: 
        raise Exception(f'Section{section} is not found in the {filename} file')
    return db

config()