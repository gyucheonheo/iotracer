#!/bin/bash

tracing=/sys/kernel/debug/tracing
index=1
count=0
option=0
fnc=0
syscall=0

function usage {
    cat <<EOF
 USAGE: ./run [-o size/flag] [-s fread|fwrite|fopen]
               -o             # Option; r,rp,w,wp,a,ap for fopen
                              # Option; 8,16,32...2.097e6+6 bytes for fread or fwrite
 eg,
        ./run -o 16 -s fread
        ./run -o 128 -s fwrite
        ./run -o ap -s fopen

 See the man page and example file for more info.
EOF
    exit
}

function die {
    echo >&2 "$@"
    exit 1
}

function warn {
    if ! eval "$@"; then
		echo >&2 "WARNING: command failed \"$@\""
    fi
}

while getopts ho:s: opt
do
    case $opt in
	o)    option=$OPTARG ;;
	s)    fnc=$OPTARG
	      ;;
	*)    usage;;
    esac
done

(( $# == 0 )) && usage
(( $# < 2 )) && usage

if [ "fopen" == ${fnc} ]; then
    syscall="SyS_open"
fi
if [ "fread" == ${fnc} ]; then
    syscall="SyS_read"
fi
if [ "fwrite" == ${fnc} ]; then
    sysacll="SyS_write"
fi

dirc=$(pwd)
cd $tracing || die "ERROR: Are you Root user? Kernel has ftrace?"

cd ${dirc} # comeback

if [ ! -d ./${fnc}/data/${fnc}_${option} ]; then
    mkdir -p ./${fnc}/data/${fnc}_${option}
fi

echo option : ${option}

if [ ! -f ./${fnc}/${fnc}_${option}.c ]; then
    echo "ERROR: file not exist!"
    exit
fi
cd ./${fnc} # go 

gcc ./${fnc}_${option}.c -o ./${fnc}_${option}

cd ${dirc} # back
index=1

while [ $index -le 1 ];
do
    echo ${syscall}
    echo "INF: Unlock existing ftrace"
    pkill cat
    ./reset-ftrace -f -q
    echo "INF: Drop caches"
    sync
    echo 3 > /proc/sys/vm/drop_caches
    touch ./${fnc}/data/${fnc}_${option}/${index}.txt

    cd ./${fnc} # go
    ./${fnc}_${option} &
    pid1=$!
    cd ../ # back
    sleep 1
    ./funcgraph -p ${pid1} -T ${syscall} > ./${fnc}/data/${fnc}_${option}/${index}.txt &
    sleep 10
    pid2=$!
    kill -9 ${pid2}
    wait $pid2
    wait $pid1
    index=$((index+1))
done
