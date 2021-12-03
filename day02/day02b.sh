#!/bin/bash
declare x=0
declare z=0
declare aim=0
function forward {(( x += $1 )); (( z += $1 * aim ));}
function back (( x -= $1 ))
function up (( aim -= $1 ))
function down (( aim += $1 ))

# don't interpret the input, simply execute it
source input02.txt

(( o = x * z ))
echo $o

