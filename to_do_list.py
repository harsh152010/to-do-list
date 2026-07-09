tasks=[]
def add():
    t=input("Enter your task :")
    tasks.append(t)

def show():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for i in range(len(tasks)):
            print(i+1, ".", tasks[i])
def remove():
    show()
    r = int(input("Enter task number : "))
    
    if 1 <= r <= len(tasks):
        tasks.pop(r-1)
        print("Task successfully removed")
    else:
        print("Invalid task number")

while True:
    print("------TO DO LIST------")
    print("\n1.Add tasks")
    print("2.See all tasks")
    print("3.Remove tasks")
    print("4.Exit")
    c=int(input("\nEnter your choice : "))
    if(c==1):
        add()
    elif(c==2):
        show()
    elif(c==3):
        remove()
    elif(c==4):
        exit()
    else:
        print("invalid option")