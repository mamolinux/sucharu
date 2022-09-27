#! /bin/bash

INKSCAPE="/usr/bin/inkscape"
OPTIPNG="/usr/bin/optipng"

SRC_FILE="assets-dark.svg"
ASSETS_DIR="assets-dark"
INDEX="assets.txt"

ulimit -s 1024

render()
{
    echo Rendering $1
    $INKSCAPE --export-id=$2 \
              --export-id-only \
              --export-filename=$1 $SRC_FILE >/dev/null \
    && $OPTIPNG -o7 --quiet $1
}

for i in `cat $INDEX`
do 
if [ -f $ASSETS_DIR/$i.png ]; then
    echo $ASSETS_DIR/$i.png exists.
else
    echo
    render $ASSETS_DIR/$i.png $i &
    # allow only to execute number of jobs in parallel
    # equal to number of processors
    if [[ $(jobs -r -p | wc -l) -gt $(nproc) ]]; then
    # wait only for first job
    wait $(jobs -p)
    fi
fi
done
exit 0
