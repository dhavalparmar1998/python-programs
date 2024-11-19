from pypdf import PdfReader

reader = PdfReader("rs.pdf")

print(len(reader.pages))

page = reader.pages[0]

print(page.extract_text())
