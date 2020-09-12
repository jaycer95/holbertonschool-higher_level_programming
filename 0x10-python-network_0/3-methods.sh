#!/bin/bash
#Show allowed mthods
curl -sI $1 | grep "Allow" | cut -d" " -f2
