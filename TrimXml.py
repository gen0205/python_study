# -*- coding: utf-8 -*-
import sys
from xml.dom.minidom import parse
from xml.parsers.expat import ExpatError

def main():
    filePath = getArgument()
    if filePath is None:
        return False
    strDom = trimXmlFile(filePath)
    if strDom is None:
        return False
    writeFile(filePath, strDom)
    return True

def getArgument():
    params = sys.argv
    length = len(params)
    if length == 2:
        return params[1]
    print "Cannnot get argument..."
    return None

def trimXmlFile(filePath):
    toPrettyXml = lambda dom: "\n".join([line for line in dom.toprettyxml().split("\n") if line.strip()])
    try:
        dom = parse(filePath)
        trimmedDom = toPrettyXml(dom)
        strTrimmedDom = str(trimmedDom)
        return strTrimmedDom
    except IOError:
        print "Not exist File..."
        print "Please check import File -> {0}".format(filePath)
        return None
    except ExpatError:
        print "Incorrect XML Format..."
        print "Please check import File -> {0}".format(filePath)
        return None

def writeFile(filePath, strDom):
    with open(filePath + ".xml", "w") as f:
        f.write(strDom)
    return

if __name__ == "__main__":
    print "--------------------"
    if main():
        print "Success!"
    print "--------------------"
    raw_input("Press Enter to exit...")
