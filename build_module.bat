@echo off
python -tt build_module.py -i
@del *.pyc
echo
echo Press any key to exit...
pause>nul
