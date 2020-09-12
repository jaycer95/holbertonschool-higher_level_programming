#!/bin/bash
#Show allowed mthods
curl -si $1 | grep "Allow" | cut -d" " -f2
