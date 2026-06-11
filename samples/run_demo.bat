@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "OUTPUT_DIR=%SCRIPT_DIR%output"

if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

python "%SCRIPT_DIR%src\demo.py"

endlocal
