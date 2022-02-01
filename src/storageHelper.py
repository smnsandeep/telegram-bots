def getCurrentBal():
    expenseFile = open("storage/expense.txt", "r")
    expenseFile.seek(0)
    return expenseFile.readline()

def updateBal(newBal):
    expenseFile = open("storage/expense.txt", "w")
    #open("storage/expense.txt", "r+")
    expenseFile.write(f"{newBal}")