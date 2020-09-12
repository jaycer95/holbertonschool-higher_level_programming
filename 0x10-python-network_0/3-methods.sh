#!/bin/bash
#Show allowed mthods
curl -si OPTIONS $1 | grep "Allow:" | cut -d" " -f2
