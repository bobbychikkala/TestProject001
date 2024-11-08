cd /d %~dp0

call .venv\Scripts\activate

pytest -s -v testCases
pip install -r requirements.txt