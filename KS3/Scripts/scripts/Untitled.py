def nodeIsInside(node, backdropNode):
    topLeftNode = [node.xpos(), node.ypos()]
    topLeftBackDrop = [backdropNode.xpos(), backdropNode.ypos()]
    bottomRightNode = [node.xpos() + node.screenWidth(), node.ypos() + node.screenHeight()]
    bottomRightBackdrop = [backdropNode.xpos() + backdropNode.screenWidth(), backdropNode.ypos() + backdropNode.screenHeight()]

    topLeft = (topLeftNode[0] >= topLeftBackDrop[0]) and (topLeftNode[1] >= topLeftBackDrop[1])
    bottomRight = (bottomRightNode[0] <= bottomRightBackdrop[0]) and (bottomRightNode[1] <= bottomRightBackdrop[1])

    return topLeft and bottomRight
    

def middleBackdrop(BDnode):
    bottomRightBackdrop = [BDnode.xpos() + BDnode.screenWidth(), BDnode.ypos() + BDnode.screenHeight()]
    topLeftBackDrop = [BDnode.xpos(), BDnode.ypos()]
    
    middleBd = [(bottomRightBackdrop[0]+ topLeftBackDrop[0])/2 , (bottomRightBackdrop[1]+ topLeftBackDrop[1])/2 ]
    
    return middleBd
    
    


def zOrderFoundry(BDnode):
    zOrderF = 0
    BackdropsInside=[]
    BiggerBackdrop=[]
    
    
    
    bottomRightBackdrop = [BDnode.xpos() + BDnode.screenWidth(), BDnode.ypos() + BDnode.screenHeight()]
    topLeftBackDrop = [BDnode.xpos(), BDnode.ypos()]

    
    
    

    for node in nuke.allNodes("BackdropNode"):
        #if node != nuke.toNode("Backdrop_Adjust9"):
        if middleBackdrop(node)[0] > topLeftBackDrop[0] and middleBackdrop(node)[0]< bottomRightBackdrop[0] and middleBackdrop(node)[1] > topLeftBackDrop[1] and middleBackdrop(node)[1] < bottomRightBackdrop[1] :
            if BDnode.screenWidth()>node.screenWidth() and BDnode.screenHeight() > node.screenHeight():
                print "Hello"
                BackdropsInside.append(node)

    
    zOrderF = min([node.knob("z_order").value() for node in BackdropsInside]) - 1


    
    return (zOrderF)


def newSelection():
    bd_this = nuke.toNode("Backdrop_Adjust9")
    for n in nuke.allNodes():
        n.setSelected(False)
    for n in bd_this.getNodes():
        n.setSelected(True)
    bd_this.setSelected(True)

def center():
    bd_this = nuke.toNode("Backdrop_Adjust9")
    bd_this['bdheight'].setValue(int(bd_this['bdheight'].value()) + 100)
    bd_this['ypos'].setValue(int(bd_this['ypos'].value()) - 100)
    bd_this['bdwidth'].setValue(int(bd_this['bdwidth'].value()) + 100)
    bd_this['xpos'].setValue(int(bd_this['xpos'].value()) - 100)
    bd_this['bdwidth'].setValue(int(bd_this['bdwidth'].value()) + 100)
    bd_this['bdheight'].setValue(int(bd_this['bdheight'].value()) + 100)
    bd_this['z_order'].setValue(zOrderFoundry(bd_this))
    newSelection()
    

center()



