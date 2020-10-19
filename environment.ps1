# .\venv\Scripts\Activate.ps1
# python -m pip install --upgrade pip
# pip install -r .\requirements.txt
# $env:PYTHONPATH = 'c:\GitHub\py.etl\templates\pg2pg'
# $env:PYTHONPATH = 'c:/GitHub/py.etl/templates/pg2pg'

# $env:PYTHONPATH = 'C:/git/py.etl/templates/config.zip'
$env:PYTHONPATH = 'C:/git/py.etl/templates'
# $env:PYTHONPATH = 'c:\GitHub\py.etl'
# $env:PYTHONPATH = 'c:/GitHub/py.etl'
cls
dir env: | Out-String -Stream | Select-String "PYTHONPATH"