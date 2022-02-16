#******************************************************************************
# Author:           Khanh Vu
# Lab:              Lab_6
# Date:             02.15.2022
# Description:      The program Name Data Viewer uses object(s) created from the Name class. This program fetches
#                   name data from a database and prints out the results to the screen.
# Inputs:           A List of Name objects whose properties are str name, str gender, int year, int count
# Outputs:          str name, str gender, int year, int count
# Sources:          Murach's Python Programming - Beginner... Chapter 14_ How to define and use your own classes
#                   CIS-133Y- Python Programming I Lecture Notes - Module 6: OOP
#******************************************************************************
from Name import Name


def main():
    # Fetch name data from the Database by calling Name.readNames() method
    listOfNameObjects = Name.readNames() # the readNames() method from the Name object return a list of Name objects

    # Print out the name data
    print("{:6} {:10} {:8} {:10}".format("Year", "Name", "Gender", "Count"))  # Print header

    for i in listOfNameObjects:             # each "i" is a Name object
        print("{:<6} {:10} {:8} {:<10}".format(i.year, i.name, i.gender, i.count))


if __name__ == "__main__":
    main()
