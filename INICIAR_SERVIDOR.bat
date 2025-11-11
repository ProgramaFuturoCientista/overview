@echo off
echo ========================================
echo   Servidor HTTP - Sistema PFC
echo ========================================
echo.
echo Iniciando servidor na porta 8001...
echo.
cd /d "%~dp0"
echo Pasta atual: %CD%
echo.
echo Abrindo navegador em 3 segundos...
timeout /t 3 /nobreak >nul
start http://localhost:8001
echo.
echo ========================================
echo   Servidor rodando em:
echo   http://localhost:8001
echo ========================================
echo.
echo Para parar o servidor: Ctrl + C
echo.
python -m http.server 8001
pause

