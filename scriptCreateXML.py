#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from xml.dom import minidom
from subprocess import check_output
import os
import subprocess

xml = minidom.Document()

#on récupère le nombre de conteneurs
command = subprocess.Popen(('docker', 'ps' , '-aq'), stdout=subprocess.PIPE)
nbConteneurs = subprocess.check_output(('wc','-l'), stdin=command.stdout)
nbConteneurs = int(nbConteneurs.strip().decode("UTF-8"))

rootElem = xml.createElement('containers')
i = 1
while i <= nbConteneurs:
    dataElem = xml.createElement('data')

    command = subprocess.Popen(('docker', 'ps' , '-aq'), stdout=subprocess.PIPE)
    head = subprocess.Popen(('head','-n',str(i)), stdin=command.stdout, stdout=subprocess.PIPE)
    tail = subprocess.check_output(('tail','-n','1'), stdin=head.stdout)
    containerID = tail.strip().decode("UTF-8")

    idElem = xml.createElement('id')
    idElem.appendChild(xml.createTextNode(containerID))

    command = subprocess.Popen(('docker', 'ps' , '-aq', '--format' , '{{.Names}}'), stdout=subprocess.PIPE)
    head = subprocess.Popen(('head','-n',str(i)), stdin=command.stdout, stdout=subprocess.PIPE)
    tail = subprocess.check_output(('tail','-n','1'), stdin=head.stdout)
    containerName = tail.strip().decode("UTF-8")

    nameElem = xml.createElement('name')
    nameElem.appendChild(xml.createTextNode(containerName))

    command = subprocess.Popen(('docker', 'ps' , '-aq', '--format' , '{{.Image}}'), stdout=subprocess.PIPE)
    head = subprocess.Popen(('head','-n',str(i)), stdin=command.stdout, stdout=subprocess.PIPE)
    tail = subprocess.check_output(('tail','-n','1'), stdin=head.stdout)
    containerImg = tail.strip().decode("UTF-8")

    imgElem = xml.createElement('img')
    imgElem.appendChild(xml.createTextNode(containerImg))

    command = subprocess.Popen(('docker', 'ps' , '-aq', '--format' , '{{.Status}}'), stdout=subprocess.PIPE)
    head = subprocess.Popen(('head','-n',str(i)), stdin=command.stdout, stdout=subprocess.PIPE)
    tail = subprocess.check_output(('tail','-n','1'), stdin=head.stdout)
    containerStatus = tail.strip().decode("UTF-8")

    statusElem = xml.createElement('status')
    statusElem.appendChild(xml.createTextNode(containerStatus))

    dataElem.appendChild(idElem)
    dataElem.appendChild(nameElem)
    dataElem.appendChild(imgElem)
    dataElem.appendChild(statusElem)

    rootElem.appendChild(dataElem)

    i = i + 1

xml.appendChild(rootElem)

xml_str = xml.toprettyxml(indent="\t")

print(xml_str)
