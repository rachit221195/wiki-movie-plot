#!/usr/bin/env bash

mkdir ../tmp
cd ../tmp

kaggle datasets download -d jrobischon/wikipedia-movie-plots
echo "Data Downloaded successfully"

unzip wikipedia-movie-plots.zip -d ../data/
echo "Data unzipped successfully"

cd ..
chmod -R 777 data/

rm -rf tmp/
