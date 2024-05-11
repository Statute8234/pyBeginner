'''
Exercise 9
Objective: create funtion voter(num); this should return the resultant nominee from a dictionary with the following assignments:
			1: Clinton; 2:Cruz; 3:Sanders; 4: Trump; 5: Kasich; 6: Rubio
			For example: voter(3) should return "Sanders"

(triple apostrophes allow strings to span multiple lines)
'''

dictionary = {
    "1": "Clinton",
    "2":"Cruz",
    "3":"Sanders",
    "4":"Trump",
    "5":"Kasich",
    "6":"Rubio"
}

def voter(num):
    find = dictionary[str(num)]
    return [find]
print(voter(3))