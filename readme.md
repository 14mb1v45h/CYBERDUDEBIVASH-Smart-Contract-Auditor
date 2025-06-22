# CYBERDUDEBIVASH Smart Contract Auditor
A web-based tool for simulating smart contract vulnerability audits.

## Features
- Input and scan Solidity code.
- Detect simulated vulnerabilities (e.g., reentrancy, integer overflow).
- Stop scan functionality.
- Export audit report as text.
- Quit button to close the app.

## How to Run
1. Save `index.html` and open in a browser, or package and run the .exe.

## Building the Executable
1. Install PyInstaller: `pip install pyinstaller`
2. Run: `pyinstaller --onefile --add-data "index.html;." cyberdudebivash-smart-contract-auditor.py`
3. Find the .exe in the `dist` folder.

## Future Improvements
- Integrate with Slither or MythX for real auditing.
- Add more vulnerability checks.