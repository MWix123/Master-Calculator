#!/bin/bash

if [ $# -ne 1 ]; then
	echo "wrong arguments"
	exit
fi

while read p; do
	touch $p
done < $1
