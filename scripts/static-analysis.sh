#!/bin/bash
set -e

echo "Running mypy..."
mypy .

echo "Running isort..."
isort .