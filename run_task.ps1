$sessions = quser | Where-Object {$_ -match 'RBP_PYTHON_01'}
$sessionIds = ($sessions -split ' +')[2]
cd "C:\Windows\PSTools\"
.\psexec -i $sessionIds \\192.168.1.43 -u WIN-K9F18NS5SAF\RBP_PYTHON_01 -p 00000000 -accepteula  cmd /c "python "C:\Jenkins\workspace\job_RBP_PYTHON_01\test_pywin.py""