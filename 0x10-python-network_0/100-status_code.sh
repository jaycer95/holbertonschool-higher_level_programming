#!/bin/bash
#send a request to a URL passed as an argument, and display only the status code of the response.
curl -sL -o /dev/null -I -w "%{http_code}" $1
