#!/usr/bin/env bash

NEWSCORES=()
OLDSCORES=()
FILENAMES=`git diff --name-only --diff-filter=M main src | grep ".*.py"`
EXITCODE=0
INDEXABLEFILENAMES=()

touch tempfile.py

for FN in ${FILENAMES[@]}; do
  INDEXABLEFILENAMES+=( $FN )
done

for FN in ${FILENAMES[@]}; do
  NEWSCORES+=( `python3 -m pylint $FN | sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p'` )
done

for FN in ${FILENAMES[@]}; do
  git show origin/$CI_DEFAULT_BRANCH:${FN} > tempfile.py
  OLDSCORES+=( `python3 -m pylint tempfile.py | sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p'` )
done

for I in ${!NEWSCORES[@]}; do
  if `python3 -c "exit(0 if ${NEWSCORES[I]} < ${OLDSCORES[I]} else 1)"`; then
    echo "New score lower than old in file ${INDEXABLEFILENAMES[I]}. New score: ${NEWSCORES[I]} Old score: ${OLDSCORES[I]}"
    EXITCODE=1
  fi
done

rm tempfile.py
exit $EXITCODE
