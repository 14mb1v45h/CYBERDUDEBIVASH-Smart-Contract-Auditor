import webbrowser
import os
import sys

def main():
    # Get the path to the executable's directory
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller executable
        base_path = sys._MEIPASS
    else:
        # Running in development
        base_path = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to index.html
    html_path = os.path.join(base_path, 'index.html')
    
    # Open the HTML file
    if os.path.exists(html_path):
        webbrowser.open('file:///' + html_path.replace('\\', '/'))
    else:
        print(f"Error: index.html not found at {html_path}")

if __name__ == "__main__":
    main()