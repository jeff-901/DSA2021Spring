#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 [problem_id]"
    exit 1
fi

problem_id=$1
mkdir "$problem_id"
mkdir "$problem_id/input"
mkdir "$problem_id/output"
mkdir "$problem_id/bin"

cp template/test.py "$problem_id"
cp template/generate.py "$problem_id"
