@echo off
title ARX CASINO LAUNCHER
color 0a
cls

echo  =======================================================
echo        ARX CASINO - LAUNCHING SYSTEM...
echo  =======================================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in your PATH!
    echo Please install Python to play.
    pause
    exit
)

:: Run the game
echo Launching casino.py...
echo.
python casino.py

:: If the game crashes or exits, pause so user can see output
if %errorlevel% neq 0 (
    echo.
    echo [SYSTEM] Application exited with an error.
    pause
) else (
    echo.
    echo [SYSTEM] Thank you for playing at ARX CASINO.
    pause
)
