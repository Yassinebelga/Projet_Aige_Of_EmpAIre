class treeNode:

    def __init__(self, status):
        self.status=status
    
    def update(self):
        return self.status
    
    def start(self):
        self.update(self)

class ctrlNode(treeNode):

    def __init__(self, status, childlist):
        self.status=status
        self.childlist=childlist                #a ctrl node has several children, thus implemented as a list

class decoNode(treeNode):

    def __init__(self, status, child):
        self.status=status
        self.child=child                        #a deco node has only one child


class leafNode(treeNode):
    pass                                        #a leaf node has no children

class Sequence(ctrlNode):

    def update(self):
        for (child) in self.childlist:
            if (child.update(child)!="success"): #if the child process returns anything but success, the sequence stops updating its branches and returns failure
                self.status="failure"
                return self.status
        
        self.status="success"  #else, the sequence updates all of its children and returns success 
        return self.status

    
class Fallback(ctrlNode):
    pass

class UntilSuccess(decoNode):
    pass

class UntilFail(decoNode):
    pass

class ForceFail(decoNode):
    
    def update(self):
        self.child.update(self.child) #I know theres a mistake here, working on it
        self.status="failure"
        return self.status

class Invert(decoNode):
    
    def update(self):
        if (self.child.update(self.child)=="success"):
            self.status="failure"
        elif (self.child.update(self.child)=="failure"):
            self.status="success"
        return self.status       

class Action(leafNode):
    pass

class Condition(leafNode):
    pass