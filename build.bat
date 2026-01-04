@echo off
echo ========================================
echo Recipe Dredger - Build Executable
echo ========================================
echo.

echo [1/4] Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
echo     Done!
echo.

echo [2/4] Checking PyInstaller...
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo     PyInstaller not found. Installing...
    pip install pyinstaller
) else (
    echo     PyInstaller found!
)
echo.

echo [3/4] Building executable...
echo     This may take 2-3 minutes...
pyinstaller recipe_dredger.spec --clean
echo.

if exist dist\Recipe_Dredger.exe (
    echo [4/4] Build complete!
    echo.
    echo ========================================
    echo SUCCESS! Your executable is ready:
    echo ========================================
    echo.
    echo Location: dist\Recipe_Dredger.exe
    echo Size:
    dir dist\Recipe_Dredger.exe | find "Recipe_Dredger.exe"
    echo.
    echo ========================================
    echo What's Next:
    echo ========================================
    echo 1. Test it: cd dist ^&^& Recipe_Dredger.exe
    echo 2. Share it: dist\Recipe_Dredger.exe
    echo 3. Package it: See BUILD_EXECUTABLE.md
    echo.
    echo ========================================
    pause
) else (
    echo.
    echo ========================================
    echo BUILD FAILED!
    echo ========================================
    echo Check the error messages above.
    echo Common fixes:
    echo 1. pip install -r requirements.txt
    echo 2. pip install pyinstaller --upgrade
    echo.
    echo See BUILD_EXECUTABLE.md for help
    echo ========================================
    pause
)
