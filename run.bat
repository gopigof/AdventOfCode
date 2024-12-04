@echo off
setlocal

:: Check if the correct number of arguments are provided
if "%~1"=="" (
    echo Error: Please provide the day as an argument.
    goto :eof
)

if "%~2"=="" (
    set YEAR=2024
) else (
    set YEAR=%~2
)

:: Set the variables for the year and day
set DAY=%~1

:: Set the path to the Python script
set SCRIPT_PATH=year_%YEAR%.day%DAY%

@REM :: Check if the script file exists
@REM if not exist "%SCRIPT_PATH%" (
@REM     echo Error: Script %SCRIPT_PATH% does not exist.
@REM     goto :eof
@REM )

:: Run the Python script
@REM python "%SCRIPT_PATH%"
python -m "%SCRIPT_PATH%"

endlocal
