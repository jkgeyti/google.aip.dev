#!/usr/bin/env bash
set -eo pipefail

#git remote add upstream https://github.com/aip-dev/google.aip.dev.git
git fetch upstream
git merge upstream/master -m "Merge remote-tracking branch 'upstream/master'"

