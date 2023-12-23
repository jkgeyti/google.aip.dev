#!/usr/bin/env bash

for f in aip/general/*.md ; do
  echo $f
  cat $f | jq -R -s '.' | jq -s -c 'join("") | {text: .}' > $f.json
done
