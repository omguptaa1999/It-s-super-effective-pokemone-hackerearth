# It-s-super-effective-pokemone-hackerearth

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
dic = {
    "super effective": {
        "Normal": [],
        "Fire": [
            "Grass",
            "Ice",
            "Bug",
            "Steel"
        ],
        "Water": [
            "Fire",
            "Ground",
            "Rock"
        ],
        "Electric": [
            "Water",
            "Flying"
        ],
        "Grass": [
            "Water",
            "Ground",
            "Rock"
        ],
        "Ice": [
            "Grass",
            "Ground",
            "Flying",
            "Dragon"
        ],
        "Fighting": [
            "Normal",
            "Ice",
            "Rock",
            "Dark",
            "Steel"
        ],
        "Poison": [
            "Grass",
            "Fairy"
        ],
        "Ground": [
            "Fire",
            "Electric",
            "Poison",
            "Rock",
            "Steel"
        ],
        "Flying": [
            "Grass",
            "Fighting",
            "Bug"
        ],
        "Psychic": [
            "Fighting",
            "Poison"
        ],
        "Bug": [
            "Grass",
            "Psychic",
            "Dark"
        ],
        "Rock": [
            "Fire",
            "Ice",
            "Flying",
            "Bug"
        ],
        "Ghost": [
            "Psychic",
            "Ghost"
        ],
        "Dragon": [
            "Dragon"
        ],
        "Dark": [
            "Psychic",
            "Ghost"
        ],
        "Steel": [
            "Ice",
            "Rock",
            "Fairy"
        ],
        "Fairy": [
            "Fighting",
            "Dragon",
            "Dark"
        ]
    },
    "normal effective": {
        "Normal": [
            "Normal",
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Fighting",
            "Poison",
            "Ground",
            "Flying",
            "Psychic",
            "Bug",
            "Dragon",
            "Dark",
            "Fairy"
        ],
        "Fire": [
            "Normal",
            "Electric",
            "Fighting",
            "Poison",
            "Ground",
            "Flying",
            "Psychic",
            "Ghost",
            "Dark",
            "Fairy"
        ],
        "Water": [
            "Normal",
            "Electric",
            "Ice",
            "Fighting",
            "Poison",
            "Flying",
            "Psychic",
            "Bug",
            "Ghost",
            "Dark",
            "Steel",
            "Fairy"
        ],
        "Electric": [
            "Normal",
            "Fire",
            "Ice",
            "Fighting",
            "Poison",
            "Psychic",
            "Bug",
            "Rock",
            "Ghost",
            "Dark",
            "Steel",
            "Fairy"
        ],
        "Grass": [
            "Normal",
            "Electric",
            "Ice",
            "Fighting",
            "Psychic",
            "Ghost",
            "Dark",
            "Fairy"
        ],
        "Ice": [
            "Normal",
            "Electric",
            "Fighting",
            "Poison",
            "Psychic",
            "Bug",
            "Rock",
            "Ghost",
            "Dark",
            "Fairy"
        ],
        "Fighting": [
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Fighting",
            "Ground",
            "Dragon"
        ],
        "Poison": [
            "Normal",
            "Fire",
            "Water",
            "Electric",
            "Ice",
            "Fighting",
            "Flying",
            "Psychic",
            "Bug",
            "Dragon",
            "Dark"
        ],
        "Ground": [
            "Normal",
            "Water",
            "Ice",
            "Fighting",
            "Ground",
            "Psychic",
            "Ghost",
            "Dragon",
            "Dark",
            "Fairy"
        ],
        "Flying": [
            "Normal",
            "Fire",
            "Water",
            "Ice",
            "Poison",
            "Ground",
            "Flying",
            "Psychic",
            "Ghost",
            "Dragon",
            "Dark",
            "Fairy"
        ],
        "Psychic": [
            "Normal",
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Ground",
            "Flying",
            "Bug",
            "Rock",
            "Ghost",
            "Dragon",
            "Fairy"
        ],
        "Bug": [
            "Normal",
            "Water",
            "Electric",
            "Ice",
            "Ground",
            "Bug",
            "Rock",
            "Dragon"
        ],
        "Rock": [
            "Normal",
            "Water",
            "Electric",
            "Grass",
            "Poison",
            "Psychic",
            "Rock",
            "Ghost",
            "Dragon",
            "Dark",
            "Fairy"
        ],
        "Ghost": [
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Fighting",
            "Poison",
            "Ground",
            "Flying",
            "Bug",
            "Rock",
            "Dragon",
            "Steel",
            "Fairy"
        ],
        "Dragon": [
            "Normal",
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Fighting",
            "Poison",
            "Ground",
            "Flying",
            "Psychic",
            "Bug",
            "Rock",
            "Ghost",
            "Dark"
        ],
        "Dark": [
            "Normal",
            "Fire",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Poison",
            "Ground",
            "Flying",
            "Bug",
            "Rock",
            "Dragon",
            "Steel"
        ],
        "Steel": [
            "Normal",
            "Grass",
            "Fighting",
            "Poison",
            "Ground",
            "Flying",
            "Psychic",
            "Bug",
            "Ghost",
            "Dragon",
            "Dark"
        ],
        "Fairy": [
            "Normal",
            "Water",
            "Electric",
            "Grass",
            "Ice",
            "Ground",
            "Flying",
            "Psychic",
            "Bug",
            "Rock",
            "Ghost",
            "Fairy"
        ]
    },
    "not very effective": {
        "Normal": [
            "Rock",
            "Steel"
        ],
        "Fire": [
            "Fire",
            "Water",
            "Rock",
            "Dragon"
        ],
        "Water": [
            "Water",
            "Grass",
            "Dragon"
        ],
        "Electric": [
            "Electric",
            "Grass",
            "Dragon"
        ],
        "Grass": [
            "Fire",
            "Grass",
            "Poison",
            "Flying",
            "Bug",
            "Dragon",
            "Steel"
        ],
        "Ice": [
            "Fire",
            "Water",
            "Ice",
            "Steel"
        ],
        "Fighting": [
            "Poison",
            "Flying",
            "Psychic",
            "Bug",
            "Fairy"
        ],
        "Poison": [
            "Poison",
            "Ground",
            "Rock",
            "Ghost"
        ],
        "Ground": [
            "Grass",
            "Bug"
        ],
        "Flying": [
            "Electric",
            "Rock",
            "Steel"
        ],
        "Psychic": [
            "Psychic",
            "Steel"
        ],
        "Bug": [
            "Fire",
            "Fighting",
            "Poison",
            "Flying",
            "Ghost",
            "Steel",
            "Fairy"
        ],
        "Rock": [
            "Fighting",
            "Ground",
            "Steel"
        ],
        "Ghost": [
            "Dark"
        ],
        "Dragon": [
            "Steel"
        ],
        "Dark": [
            "Fighting",
            "Dark",
            "Fairy"
        ],
        "Steel": [
            "Fire",
            "Water",
            "Electric",
            "Steel"
        ],
        "Fairy": [
            "Fire",
            "Poison",
            "Steel"
        ]
    },
    "no effect": {
        "Normal": [
            "Ghost"
        ],
        "Fire": [],
        "Water": [],
        "Electric": [
            "Ground"
        ],
        "Grass": [],
        "Ice": [],
        "Fighting": [
            "Ghost"
        ],
        "Poison": [
            "Steel"
        ],
        "Ground": [
            "Flying"
        ],
        "Flying": [],
        "Psychic": [
            "Dark"
        ],
        "Bug": [],
        "Rock": [],
        "Ghost": [
            "Normal"
        ],
        "Dragon": [
            "Fairy"
        ],
        "Dark": [],
        "Steel": [],
        "Fairy": []
    }
}


n1 = int(input())
n2 = int(input())
t1 = []
t2 = []
for i in range(n1):
        t1.append(input())
for i in range(n2):
        t2.append(input())
dic_rev={}
dic_rev[2]=dic['super effective']
dic_rev[1]=dic['normal effective']
dic_rev[0.5]=dic["not very effective"]
dic_rev[0]=dic['no effect']
def points_calc(t1,t2):
    s=0
    for i in t1:
        a=(i.split(" "))
        for j in t2:
            b=j.split(" ")
            result=[]
            for k in a:
                point=1
                for l in b:
                    point=point*points(k,l)
                result.append(point)
            s=s+max(result)
    return float(s)          
def points(a,b):
    for i,j in dic_rev.items():
        if a in j.keys():
            if b in dic_rev[i][a]:
                break
    return i
def out(t1,t2):
    print(points_calc(t1,t2))
    print(points_calc(t2,t1))
    if(points_calc(t1,t2)>points_calc(t2,t1)):
        print("ME")
    if(points_calc(t1,t2)<points_calc(t2,t1)):
        print("FOE")
    if(points_calc(t1,t2)==points_calc(t2,t1)):
        print("EQUAL")
    return
out(t1,t2)
