#!/bin/bash

#utilisation de xml_grep necessite l'installation de xml-twig-tools
img=`xml_grep 'image' /home/docker/DockerScripts/container.conf.xml --text_only`

nb=`xml_grep 'number' /home/docker/DockerScripts/container.conf.xml --text_only`

i=0

xmlFile="/home/docker/DockerScripts/containers.info.xml"

echo "Création de $nb contenuer(s) $img en cours ..."

echo '<?xml version="1.0" encoding="UTF-8"?>' > $xmlFile

while [ $i -lt $nb ]
do
	
	docker run -d $img

	id=`docker ps -q`
	name=`docker ps --format "{{.Names}}"`
	img=`docker ps --format "{{.Image}}"`
	etat=`docker ps --format "{{.Status}}"`

	echo '<container>' >> $xmlFile
	echo '	<id>'"$id"'</id>' >> $xmlFile
	echo '	<nom>'"$name"'</nom>' >> $xmlFile
	echo '	<image>'"$img"'</image>' >> $xmlFile
	echo '	<etat>'"$etat"'</etat>' >> $xmlFile
	echo '</container>' >> $xmlFile

	i=$(( $i + 1 ))
done

echo "Création de $nb contenuer(s) $img terminé avec succes !"

echo 'Envoi du Fichier XML en cours ...'

scp /home/docker/DockerScripts/containers.info.xml root@192.168.0.130:/var/www/pageDeGestion/html/containers.info.xml

echo 'Envoi du Fichier XML terminé ...'





