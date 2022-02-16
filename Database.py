#******************************************************************************
# Author:           Khanh Vu
# Lab:              Lab_6 - Defining Database class
# Date:             02.15.2022
# Description:      The Database class is stored in a module named Database (Database.py). This file is just a
#                   "stubbed" in this program since we will learn how to fetch data from a database in the future.
#                   This code defines a class method called readNames(). When readName() is called, it returns a list
#                   containing at least 4 dictionary objects with name data.

# Sources:          Murach's Python Programming - Beginner... Chapter 14_ How to define and use your own classes
#                   CIS-133Y- Python Programming I Lecture Notes - Module 6: OOP
#******************************************************************************

class Database:
    @classmethod
    def readNames(cls):
        # Create at least 4 name dictionary objects
        nameDict1 = {"name": "John", "gender": "M", "year": 1915, "count": 47577}
        nameDict2 = {"name": "John", "gender": "M", "year": 1916, "count": 50046}
        nameDict3 = {"name": "John", "gender": "M", "year": 1917, "count": 51851}
        nameDict4 = {"name": "John", "gender": "M", "year": 1918, "count": 56559}
        nameDict5 = {"name": "John", "gender": "M", "year": 1919, "count": 53532}

        #Create a list that contains name dictionary objects created above

        nameData = [nameDict1, nameDict2, nameDict3, nameDict4, nameDict5]

        return nameData
