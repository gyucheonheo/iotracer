#!/bin/bash

index=1
count=0
size=8

while [ $count -le 18 ];
do
    if [ ! -d ./data/fwrite_${size} ]; then
	mkdir -p ./data/fwrite_${size}
    fi
    echo size : ${size}

    gcc fwrite_${size}.c -o fwrite_${size}
    index=1
    while [ $index -le 10 ];
    do
	pkill cat
	./reset-ftrace -f -q
	touch ./data/fwrite_${size}/${index}.txt
	./fwrite_${size} &
	pid1=$!
	sleep 6
	./funcgraph -p ${pid1} -T SyS_write > ./data/fwrite_${size}/${index}.txt &
	sleep 10
	pid2=$!
	kill -9 ${pid2}
	wait $pid2
	wait $pid1
	index=$((index+1))
    done
    
    size=$((size*2))
    count=$((count+1))
done
