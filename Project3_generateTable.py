#This Project is to create multiple multiplication table files all at once and store them in different folders in the PC:

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)




for i in range(2, 21):
    generateTable(i)