if [ `git diff --name-only --diff-filter=A master src | grep ".*.py" | wc -l` -ge 1 ]; 
then
      python3 -m pylint `git diff --name-only --diff-filter=A $CI_DEFAULT_BRANCH src | grep ".*.py"` --fail-under=10;
      fi
