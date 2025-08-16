"""
Convert Final Project Report to PDF
This script converts the Final_Project_Report.md to a PDF file.

Requirements:
pip install markdown
pip install pdfkit

Also requires wkhtmltopdf:
- Windows: Download from https://wkhtmltopdf.org/downloads.html
- Linux: sudo apt-get install wkhtmltopdf
- Mac: brew install --cask wkhtmltopdf
"""

import markdown
import pdfkit
import os

def convert_md_to_pdf(md_file, pdf_file):
    """Convert markdown file to PDF with styling."""
    
    # Read markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'tables'])
    
    # Add CSS styling
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            h1, h2, h3 {{
                color: #2c3e50;
                margin-top: 1.5em;
            }}
            h1 {{
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
                font-size: 2em;
            }}
            h2 {{
                border-bottom: 1px solid #bdc3c7;
                padding-bottom: 5px;
                font-size: 1.5em;
            }}
            h3 {{
                font-size: 1.2em;
                color: #34495e;
            }}
            code {{
                background-color: #f5f5f5;
                padding: 2px 4px;
                border-radius: 3px;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 0.9em;
            }}
            pre {{
                background-color: #f5f5f5;
                padding: 10px;
                border-radius: 5px;
                overflow-x: auto;
                border-left: 3px solid #3498db;
            }}
            blockquote {{
                border-left: 4px solid #3498db;
                padding-left: 1em;
                margin-left: 0;
                color: #555;
                font-style: italic;
            }}
            strong {{
                color: #2c3e50;
                font-weight: 600;
            }}
            ul, ol {{
                margin-left: 20px;
            }}
            li {{
                margin-bottom: 5px;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 1em 0;
            }}
            table th, table td {{
                border: 1px solid #ddd;
                padding: 10px;
                text-align: left;
            }}
            table th {{
                background-color: #3498db;
                color: white;
                font-weight: bold;
            }}
            table tr:nth-child(even) {{
                background-color: #f5f5f5;
            }}
            hr {{
                border: none;
                border-top: 2px solid #bdc3c7;
                margin: 2em 0;
            }}
            em {{
                color: #7f8c8d;
            }}
            p {{
                margin-bottom: 1em;
                text-align: justify;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # PDF options
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None
    }
    
    # Convert HTML to PDF
    try:
        pdfkit.from_string(styled_html, pdf_file, options=options)
        print(f"✅ Successfully converted {md_file} to {pdf_file}")
    except Exception as e:
        print(f"❌ Error converting to PDF: {e}")
        print("Make sure wkhtmltopdf is installed and in your PATH")
        
        # Alternative: Save as HTML if PDF conversion fails
        html_file = pdf_file.replace('.pdf', '.html')
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(styled_html)
        print(f"💾 Saved as HTML instead: {html_file}")

if __name__ == "__main__":
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define file paths
    md_file = os.path.join(current_dir, "Final_Project_Report.md")
    pdf_file = os.path.join(current_dir, "Final_Project_Report.pdf")
    
    # Check if markdown file exists
    if os.path.exists(md_file):
        convert_md_to_pdf(md_file, pdf_file)
    else:
        print(f"❌ Error: {md_file} not found!")
        print("Make sure the Final_Project_Report.md file is in the same directory as this script.")
