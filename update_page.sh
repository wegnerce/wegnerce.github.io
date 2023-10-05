#!/usr/bin/env bash

pelican content -o output -s pelicanconf.py

ghp-import -m "Update webpage 2021/04" output

git push -f http://github.com/wegnerce/wegnerce.github.io.git gh-pages:master
