pip install pyinstaller
pip freeze > 'requirements.txt'
pyinstaller –name="VsCalculator" --noconfirm --onefile --add-data='files/:files' --icon='files/ecop.png' --noconsole --clean --log-level=WARN main.py
