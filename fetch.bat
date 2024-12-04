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

:: Set the challenge URL (replace with the actual URL of the test data)
set CHALLENGE_URL="https://adventofcode.com/%YEAR%/day/%DAY%/input"

:: Set the output file name
set OUTPUT_FILE=data\year_%YEAR%\day%DAY%_input.txt
set OUTPUT_TEST_FILE=data\year_%YEAR%\day%DAY%_test.txt
set PY_FILE=year_%YEAR%\day%DAY%.py

:: Download the data using curl
curl --create-dirs -o %OUTPUT_FILE% %CHALLENGE_URL% --compressed ^
    -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0" ^
    -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ^
    -H "Accept-Language: en-US,en;q=0.5" ^
    -H "Accept-Encoding: gzip, deflate, br, zstd" ^
    -H "Referer: https://adventofcode.com/2024/day/1" ^
    -H "DNT: 1" ^
    -H "Connection: keep-alive" ^
    -H "Cookie: session=<FILL ME>" ^
    -H "Upgrade-Insecure-Requests: 1" ^
    -H "Sec-Fetch-Dest: document" ^
    -H "Sec-Fetch-Mode: navigate" ^
    -H "Sec-Fetch-Site: same-origin" ^
    -H "Sec-GPC: 1" ^
    -H "Priority: u=0, i" ^
    -H "Pragma: no-cache"  ^
    -H "Cache-Control: no-cache"


if errorlevel 1 (
    echo Failed to download the data. Please check the URL and try again.
) else (
    echo Data downloaded successfully to %OUTPUT_FILE%
)

copy NUL %OUTPUT_TEST_FILE%

:: Create each challenge solution file using the pre-defined script in Pycharm scratches
type commons\base_solution.py >> %PY_FILE%


endlocal
