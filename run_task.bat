cd "C:\Windows\PSTools\"
for /f "tokens=3 skip=1" %a in ('qwinsta RBP_PYTHON_01') do set "userid=%a"
echo %userid%
psexec -i %userid% \\192.168.1.43 -u WIN-K9F18NS5SAF\RBP_PYTHON_01 -p 00000000 -accepteula  cmd /c "python "C:\Jenkins\workspace\job_RBP_PYTHON_01\test_pywin.py""
