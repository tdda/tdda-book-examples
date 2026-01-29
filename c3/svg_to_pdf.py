#!/usr/bin/env python3

import sys
import os
import tempfile
import subprocess
import time

def convert_svg_to_pdf(svg_file):
    if not os.path.exists(svg_file):
        print(f"Error: File '{svg_file}' not found")
        return False
    
    if not svg_file.endswith('.svg'):
        print(f"Error: '{svg_file}' is not an SVG file")
        return False
    
    # Get paths
    dir_name = os.path.dirname(os.path.abspath(svg_file))
    base_name = os.path.splitext(os.path.basename(svg_file))[0]
    pdf_file = os.path.join(dir_name, f"{base_name}.pdf")
    abs_svg_path = os.path.abspath(svg_file)
    
    print(f"Converting '{svg_file}' to '{pdf_file}'...")
    
    # Create a more targeted AppleScript that handles the save location properly
    applescript = f'''
    set svgPath to "{abs_svg_path}"
    set pdfPath to "{pdf_file}"
    set pdfDir to "{dir_name}"
    set pdfName to "{base_name}"
    
    tell application "Safari"
        activate
        open location ("file://" & svgPath)
        delay 4
    end tell
    
    tell application "System Events"
        tell process "Safari"
            -- Open print dialog
            keystroke "p" using command down
            delay 3
            
            -- Make sure we're in the print dialog
            repeat while not (exists sheet 1 of front window)
                delay 0.5
            end repeat
            
            -- Use keyboard-only approach to avoid UI element detection issues
            -- Press Command+Return which should default to "Save as PDF"
            keystroke return using command down
            delay 3
            
            -- Check if we're now in a save dialog
            if exists sheet 1 of sheet 1 of front window then
                tell sheet 1 of sheet 1 of front window
                    -- Navigate to directory using Command+Shift+G
                    keystroke "g" using {{shift down, command down}}
                    delay 2
                    
                    -- Type the directory path directly
                    keystroke pdfDir
                    delay 1
                    keystroke return
                    delay 3
                    
                    -- Enter filename (select all first to clear any existing text)
                    keystroke "a" using command down
                    delay 0.5
                    keystroke pdfName
                    delay 1
                    
                    -- Save the file
                    keystroke return
                    delay 4
                end tell
            else
                -- Fallback: maybe the print dialog is still open, try different approach
                -- Look for any button with "PDF" in its name and click it
                try
                    set pdfButtons to every button of sheet 1 of front window whose name contains "PDF"
                    if length of pdfButtons > 0 then
                        click item 1 of pdfButtons
                        delay 2
                        -- Continue with save process
                        keystroke "g" using {{shift down, command down}}
                        delay 1
                        keystroke pdfDir
                        keystroke return
                        delay 2
                        keystroke "a" using command down
                        keystroke pdfName
                        keystroke return
                        delay 3
                    end if
                on error
                    -- Last resort: just escape out
                    key code 53 -- Escape
                end try
            end if
            
            -- Close Safari tab
            keystroke "w" using command down
        end tell
    end tell
    '''
    
    try:
        # Execute AppleScript with explicit timeout
        result = subprocess.run(
            ['osascript', '-e', applescript], 
            capture_output=True, 
            text=True, 
            timeout=45
        )
        
        if result.returncode != 0:
            print(f"AppleScript execution failed: {result.stderr}")
            return False
        
        # Wait a moment for file system to settle
        time.sleep(3)
        
        # Check if PDF was created at the exact location we specified
        if os.path.exists(pdf_file):
            print(f"✓ Successfully created '{pdf_file}'")
            return True
        else:
            print(f"✗ Failed to create '{pdf_file}' at specified location")
            print("The print dialog may have appeared but the save operation failed")
            return False
            
    except subprocess.TimeoutExpired:
        print("AppleScript timed out - the print dialog may have gotten stuck")
        return False
    except Exception as e:
        print(f"Error executing AppleScript: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 svg_to_pdf.py file1.svg [file2.svg ...]")
        print("Example: python3 svg_to_pdf.py image.svg")
        print("")
        print("This script uses Safari specifically to convert SVG to PDF")
        print("with proper scaling to fit one page.")
        sys.exit(1)
    
    for svg_file in sys.argv[1:]:
        convert_svg_to_pdf(svg_file)
    
    print("Done!")

if __name__ == "__main__":
    main()
