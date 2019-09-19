#!/bin/bash


	pkill cat
	./reset-ftrace -f -q
	touch ./data/simple/test.dat
	./simple &
	pid1=$!
	echo ${pid1}
	sleep 1
	./funcgraph -p ${pid1} SyS_open > ./data/simple/test.dat &
	sleep 1
	pid2=$!

	kill -9 ${pid2}

	wait $pid2
	wait $pid1

echo 'The loop has ended.'
