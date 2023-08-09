#!/bin/bash
cd ../source
python3 -m pytest --ignore Tests/otlLib/optimize_test.py --ignore Tests/varLib/merger_test.py --ignore Tests/varLib/varLib_test.py
