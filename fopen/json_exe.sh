#!/bin/bash

for file in ./xmls/*
do
    name=$(basename ${file} .xml)
    echo ${name}
    cd ./anychart_jsons
    ~/dropbox_uploader.sh upload ${name}.json ./anychart_jsons/fopen/${name}.json
    cd ../
done


    
