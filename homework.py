import cgi
import cgitb; cgitb.enable()   # for pretty error messages
import os
import time

from support import *
from UPGMA import *


def randomName():
    filename = str(int(time.time()))
    return filename

def saveTree(filename, tree):
    savefile = file(filename, "w")
    print >> savefile, tree
    savefile.close()


def main():
    # extract the form submitted by the user
    form = cgi.FieldStorage()


    try:
        data = form["matrix"].value.strip()
        method = form["type"].value.strip()
        if method == "mat":
            M, tags = getMatrix(data)
        if method == "sequence":
            M, tags = distanceTaxa(data)
    except:
        print "Content-type: text/html"
        print
        print "<big>" "<b>" "<center>" "Sorry! Your data is not in the correct format. Please check your data entry and try again." "</center>" "</b>" "</big>"
        print "<br/>"
        print "<big>" "<b>" "<center> ""If you are not sure about how to format entries, see the tutorial for help""</center>" "</b>" "</big>"
        print "<br/>"
        print "<br/>"
        print "<br/>"
        print "<center>" "<img src='SadBaby.bmp' width='500' height='500' alt='Sad Baby'>" "</center>"
        return
    
    tree = buildTree(M, tags)
    saveTree("output/phylip-intree.txt", tree)

    name = randomName()
    os.system("cd output; /usr/local/phylip/bin/drawgram < ../phylip-script-bmp.txt > /dev/null 2>&1")
    os.system("cd output; mv plotfile plotfile-%s.bmp" % name)
    
    print "Content-type: text/html"
    print
    print "<b>" "<center>" "<bing>" "DATA OUTPUT" "</bing>" "</center>" "</b>" 
    print "<p />"
    print "<br />"
    print "<b>" "PHYLIP Format:" "</b>", tree
    print "<p />"
    print "<br />"
    print "<br />"
    print "<b>" "YOUR TREE" "</b>"
    print "<p />"
    print "<img src='output/plotfile-%s.bmp' width='500' height='500' alt='Phylogenetic tree'>" % name

    


main()