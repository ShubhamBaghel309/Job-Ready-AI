# Installation Instructions

1. Install Python Requirements:
```bash
pip install -r requirements.txt
```

2. Install wkhtmltopdf:
- Download the installer from: https://wkhtmltopdf.org/downloads.html
- Choose the Windows installer (64-bit)
- Run the installer and follow the installation wizard
- Add the installation directory (usually `C:\Program Files\wkhtmltopdf\bin`) to your system PATH

3. Verify Installation:
```bash
wkhtmltopdf --version
```

If you see the version number, the installation was successful.

## Troubleshooting

If you get a "wkhtmltopdf not found" error:
1. Make sure wkhtmltopdf is installed
2. Verify the PATH environment variable includes the wkhtmltopdf bin directory
3. Try restarting your terminal/IDE after installation
