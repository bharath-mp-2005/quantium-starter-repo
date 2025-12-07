#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate 2>/dev/null || source venv/bin/activate

# Run tests
pytest
RESULT=$?

# If tests passed
if [ $RESULT -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi
