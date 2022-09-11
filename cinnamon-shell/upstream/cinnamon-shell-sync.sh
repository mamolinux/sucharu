#!/usr/bin/env bash
# -*- coding: UTF-8 -*-
## Helper script to sync Mint-Y from upstream to a destination folder
## usage:
##
##      cinnamon-shell-sync.sh --destination <path>
##
## options:
##    -d, --destination <path>    Destination folder - mandatory
##    -b, --branch <name>         Branch name
# CLInt GENERATED_CODE: start

# No-arguments is not allowed
[ $# -eq 0 ] && sed -ne 's/^## \(.*\)/\1/p' $0 && exit 1

# Converting long-options into short ones
for arg in "$@"; do
  shift
  case "$arg" in
"--destination") set -- "$@" "-d";;
"--branch") set -- "$@" "-b";;
  *) set -- "$@" "$arg"
  esac
done

function print_illegal() {
    echo Unexpected flag in command line \"$@\"
}

# Parsing flags and arguments
while getopts 'hab:d:' OPT; do
    case $OPT in
        h) sed -ne 's/^## \(.*\)/\1/p' $0
           exit 1 ;;
        d) _destination=$OPTARG ;;
        b) _branch=$OPTARG ;;
        \?) print_illegal $@ >&2;
            echo "---"
            sed -ne 's/^## \(.*\)/\1/p' $0
            exit 1
            ;;
    esac
done
# CLInt  GENERATED_CODE: end

wget_check=`which wget | wc -l`
[ $wget_check == 0 ] && echo "install wget" && exit 1


_branch=${_branch:=master}
data=https://raw.githubusercontent.com/linuxmint/mint-themes/${_branch}/src/Mint-Y
root=${data}/cinnamon

[ ! -d ${_destination} ] && echo ${_destination} folder does not exists && exit 1
[ ! -d ${_destination}/sass ] && mkdir ${_destination}/sass

files=(
  sass/cinnamon.scss
  sass/cinnamon-dark.scss
  sass/_colors.scss
  sass/_common.scss
  sass/_drawing.scss
  README.md
)

set -e
for i in ${files[@]}; do
    wget ${root}/${i} -O ${_destination}/${i}
done

# assets=(
# )

# if [ ! -z $_assets ]; then
#     for i in ${assets[@]}; do
#         wget ${root}/assets/${i} -O ${_destination}/assets/${i}
#     done
# fi
