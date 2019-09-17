#!/bin/bash

declare -a flags=("fopen_r" "fopen_rp" "fopen_w" "fopen_wp" "fopen_a" "fopen_ap")

for item in "${flags[@]}";
do
    if [ ! -d ./data/"$item" ]; then
	mkdir -p ./data/"$item"
    fi

    gcc "$item".c -o "$item"

    echo "=>BEGIN $item"
    count=0
    while [ $count -le 0 ];
    do
	echo "==>${count}"
	pkill cat
	./reset-ftrace -f -q
	touch ./data/"$item"/test_${count}.dat
	./"$item" &
	pid1=$!
	echo ${pid1}
	sleep 1
	./funcgraph -p ${pid1} -T SyS_open > ./data/"$item"/test_${count}.dat &
	sleep 1
	pid2=$!
	echo funcgraph ${pid2}
	kill -9 ${pid2}

	wait $pid2
	wait $pid1
	count=$((count+1))
    done
    echo "<=END $item"
done

echo 'The loop has ended.'
