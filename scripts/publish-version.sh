#!/usr/bin/env bash

# Exit on first error
set -e


##
## Check different preconditions
##

# Check there is one argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 version_number" >&2
    exit 1
fi

# Not starting with 'v'
if [[ "$1" == v* ]]; then
    echo "Version number should not start with 'v'" >&2
    exit 1
fi

# Check if the repository is clean (ignoring untracked)
# see: https://unix.stackexchange.com/a/394674
git diff-index --quiet HEAD


##
## Upload a new version of the recipe
##
conan export conanfile.py $1@adnn/stable
conan upload -r adnn shred_conan_base/$1@adnn/stable
