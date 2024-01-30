import html2text
import pdfplumber
from tqdm import tqdm

# Open the PDF file
with pdfplumber.open(
    "document/Digital Image Processing (Rafael C. Gonzalez, Richard E. Woods) (Z-Library).pdf"
) as pdf:
    # Initialize a Markdown converter
    h = html2text.HTML2Text()
    h.ignore_links = True

    markdown = ""
    # Loop through each page in the PDF
    for page in tqdm(pdf.pages):
        # Extract the text as HTML
        width, height = page.width, page.height
        # Get the region excluding the header
        main_box = (width * 0.05, height * 0.1, width * 0.95, height * 0.9)
        # Extract the text from the main region
        html = page.crop(main_box, relative=True).extract_text()
        # Convert the HTML to Markdown
        markdown += h.handle(html)
        # Print the Markdown
    
    with open("out.md", "w+", encoding="utf-8") as f:
        f.write(markdown)
