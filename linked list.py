class linkedlist:
    def __init__(self, value, nextvalue=None):
        self.value=value
        self.nextvalue=nextvalue
    
node1=linkedlist(1)
node2=linkedlist(2)
node1.nextvalue=node2

currentnode=node1
while True:
    print(currentnode.value,"->",end=" ")
    if currentnode.nextvalue == None:
        print("none")
        break
    currentnode=currentnode.nextvalue
#------------------------------------------------------