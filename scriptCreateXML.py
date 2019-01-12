#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from xml.dom import minidom
from xml.dom.minidom import Document
from subprocess import check_output

xml = minidom.Document()

rootElem = xml.createElement('containers')

dataElem = xml.createElement('data')

containerID = check_output(["docker", "ps", "-aq"]).strip().decode("UTF-8")
idElem = xml.createElement('id')
idElem.appendChild(xml.createTextNode(containerID))

containerName = check_output(["docker", "ps","-a", "--format", "{{.Names}}"]).strip().decode("UTF-8")
nameElem = xml.createElement('name')
nameElem.appendChild(xml.createTextNode(containerName))

containerImg = check_output(["docker", "ps", "-a", "--format", "{{.Image}}"]).strip().decode("UTF-8")
imgElem = xml.createElement('img')
imgElem.appendChild(xml.createTextNode(containerImg))

containerStatus = check_output(["docker", "ps", "-a", "--format", "{{.Status}}"]).strip().decode("UTF-8")
statusElem = xml.createElement('status')
statusElem.appendChild(xml.createTextNode(containerStatus))

dataElem.appendChild(idElem)
dataElem.appendChild(nameElem)
dataElem.appendChild(imgElem)
dataElem.appendChild(statusElem)

rootElem.appendChild(dataElem)

xml.appendChild(rootElem)

xml_str = xml.toprettyxml(indent="\t")

save_path_file = "retour.xml"

with open (save_path_file, "w") as f:
    f.write(xml_str)

print("Creation du fichier XML de retour terminé !")
