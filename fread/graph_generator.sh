#!/bin/bash

tracing=/sys/kernel/debug/tracing
flock=/var/tmp/.ftrace-lock

trap ':' INT QUIT TERM PIPE HUP 

function warn {
	 if ! eval "$@"; then
	      echo >&2 "WARNING: command failed \"$@"\"
	 fi
}


function end {
    echo 2>/dev/null
    echo "Ending tracing..." 2>/dev/null
    cd $tracing

    (( opt_time )) && warn "echo nofuncgraph-abstime > trace_options"
    (( opt_proc )) && warn "echo nofuncgraph-proc > trace_options"
    (( opt_tail )) && warn "echo nofuncgraph-tail > trace_options"
    (( opt_nodur )) && warn "echo funcgraph-duration > trace_options"
    (( opt_cpu )) && warn "echo sleep-time > trace_options"
    warn "echo nop > current_tracer"
    (( opt_pid || opt_tid )) && warn "echo > set_ftrace_pid"
    (( opt_max )) && warn "echo 0 > max_graph_depth"
    warn "echo > set_graph_function"
    warn "echo > trace"
    (( wroteflock )) && warn "rm $flock"
}


