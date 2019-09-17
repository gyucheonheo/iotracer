#!/bin/bash

index=1
count=0
size=1024

if [ ! -d ./data/fread_${size} ]; then
    mkdir -p ./data/fread_${size}
fi
echo size : ${size}

gcc fread_${size}.c -o fread_${size}

index=1
while [ $index -le 10 ];
do
    pkill cat
    ./reset-ftrace -f -q
    touch ./data/fread_${size}/${index}.txt
    ./fread_${size} &
    pid1=$!
    sleep 6
    ./funcgraph -p ${pid1} -T SyS_read > ./data/fread_${size}/${index}.txt &
    sleep 10
    pid2=$!
    kill -9 ${pid2}
    wait $pid2
    wait $pid1
    index=$((index+1))
done


#if [ ! -d ./data/fwrite_${size} ]; then
#    mkdir -p ./data/fwrite_${size}
#fi

#pkill cat
#./reset-ftrace -f -q
#touch ./data/simple.dat
#	./fwrite_t &
#	pid1=$!
#	echo ${pid1}
#	sleep 6
#	./funcgraph -p ${pid1} SyS_write > ./data/simple.dat &
#	sleep 10
#	pid2=$!
#	echo funcgraph ${pid2}
#	kill -9 ${pid2}

#	wait $pid2
#	wait $pid1
#echo 'The loop has ended.'
