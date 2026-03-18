@echo off
REM Ejecutar el script de Python
python convertir_subir.py

REM Agregar todos los cambios al repositorio
git add .

REM Crear un commit con mensaje automático
git commit -m "Actualización automática de HTML e índice"

REM Subir los cambios a GitHub
git push origin main

echo.
echo Proceso completado: los archivos se han convertido y subido a GitHub.
pause