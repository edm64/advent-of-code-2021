#!/bin/bash
declare x=0
declare z=0
function forward (( x += $1 ))
function back (( x -= $1 ))
function up (( z -= $1 ))
function down (( z += $1 ))

# don't interpret the input, simply execute it
source input02.txt

(( o = x * z ))
echo $o

