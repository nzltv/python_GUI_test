cd "C:\Windows\PSTools\"
psexec -i 3 \\192.168.1.43 -u WIN-K9F18NS5SAF\RBP_PYTHON_01 -p 00000000 -accepteula  cmd /c "python "C:\Jenkins\workspace\job_RBP_PYTHON_01\test_pywin.py""
