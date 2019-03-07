# -*- coding: UTF-8 -*-

from xml.dom import minidom
import subprocess

def getNbContainers():
    nbContainers = subprocess.Popen(('docker', 'ps' , '-aq'), stdout=subprocess.PIPE)
    nbContainers = subprocess.check_output(('wc','-l'), stdin=nbContainers.stdout)
    nbContainers = int(nbContainers.strip().decode("UTF-8"))
    return nbContainers

def getContainersID():
    containersID = subprocess.check_output(('docker', 'ps' , '-aq'))
    containersID = containersID.strip().decode("UTF-8")
    containersID = containersID.split("\n")
    return containersID

def getContainersNames():
    containersNames = subprocess.check_output(('docker', 'ps' , '-aq', '--format' , '{{.Names}}'))
    containersNames = containersNames.strip().decode("UTF-8")
    containersNames = containersNames.split("\n")
    return containersNames

def getContainersImages():
    containersImages = subprocess.check_output(('docker', 'ps' , '-aq', '--format' , '{{.Image}}'))
    containersImages = containersImages.strip().decode("UTF-8")
    containersImages = containersImages.split("\n")
    return containersImages

def getContainersStatus():
    containersStatus = subprocess.check_output(('docker', 'ps' , '-aq', '--format' , '{{.Status}}'))
    containersStatus = containersStatus.strip().decode("UTF-8")
    containersStatus = containersStatus.split("\n")
    return containersStatus

def getContainersIP(nbContainers):
    containersIP  = None
    if nbContainers > 0:
        containersIP = subprocess.Popen(('docker', 'ps' , '-aq'), stdout=subprocess.PIPE)
        containersIP = subprocess.check_output(('xargs', 'docker', 'inspect', '--format', '"{{ .NetworkSettings.IPAddress }}"'), stdin=containersIP.stdout)
        containersIP = containersIP.strip().decode("UTF-8")
        containersIP = containersIP.replace('""','No IP')
        containersIP = containersIP.replace('"','')
        containersIP = containersIP.split("\n")
    return containersIP

def main():

    xml = minidom.Document()

    nbContainers = getNbContainers()

    containersID = getContainersID()
    containersNames = getContainersNames()
    containersImages = getContainersImages()
    containersStatus = getContainersStatus()
    containersIP = getContainersIP(nbContainers)

    rootElem = xml.createElement('containers')
    i = 0

    while i < nbContainers:

        dataElem = xml.createElement('data')

        idElem = xml.createElement('id')
        nameElem = xml.createElement('name')
        imgElem = xml.createElement('img')
        statusElem = xml.createElement('status')
        ipElem = xml.createElement('ip')

        idElem.appendChild(xml.createTextNode(containersID[i]))
        nameElem.appendChild(xml.createTextNode(containersNames[i]))
        imgElem.appendChild(xml.createTextNode(containersImages[i]))
        statusElem.appendChild(xml.createTextNode(containersStatus[i]))
        ipElem.appendChild(xml.createTextNode(containersIP[i]))

        dataElem.appendChild(idElem)
        dataElem.appendChild(nameElem)
        dataElem.appendChild(imgElem)
        dataElem.appendChild(statusElem)
        dataElem.appendChild(ipElem)

        rootElem.appendChild(dataElem)

        i = i + 1

    xml.appendChild(rootElem)

    xml_str = xml.toprettyxml(indent="\t")

    print(xml_str)

if __name__ == '__main__':
    main()
