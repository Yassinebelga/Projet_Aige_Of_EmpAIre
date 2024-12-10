class treeNode:

    def _init_(self, status):
        pass

    def start():
        pass
    
    def update():
        pass


class ctrlNode(treeNode):
    pass

class decoNode(treeNode):
    pass

class leafNode(treeNode):
    pass

class Sequence(ctrlNode):
    pass

class Fallback(ctrlNode):
    pass

class UntilSuccess(decoNode):
    pass

class UntilFail(decoNode):
    pass

class ForceFail(decoNode):
    pass

class Invert(decoNode):
    pass

class Action(leafNode):
    pass

class Condition(leafNode):
    pass