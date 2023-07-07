#!/usr/bin/env sh -x

# Make zip file with empty things.
rm lambda.zip
mkdir target

# Include py files in zip exclude venv folder.
cp ./* target
rm -rf target/venv target/.git target/.gitignore target/build_lambda_zip.sh target/.idea target/README.md target/requirements.txt
cp -r ./venv/lib/python3.10/site-packages/* target

# Zip it.
cd target
rm -rf ./boto* ./PIL ./mysqlclient ./MySQLdb
zip -r ../lambda.zip .
rm -rf ../target