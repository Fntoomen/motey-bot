#!/bin/sh
# Remove your token from the entire repo history
git filter-repo --force --replace-text <(echo 'XYZ==>TOKEN')
