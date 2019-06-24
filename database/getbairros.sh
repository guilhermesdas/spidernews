#!/bin/bash


curl -X POST 'https://places-dsn.algolia.net/1/places/query' \
  --data '{"query": "Manaus ufam","hitsPerPage":"1","countries": ["br"],"language":"pt","type": "address"}' > bairros

python bairros.py