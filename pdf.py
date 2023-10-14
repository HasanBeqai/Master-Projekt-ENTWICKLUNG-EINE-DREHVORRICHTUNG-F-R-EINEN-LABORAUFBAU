import PyPDF2

writer = PyPDF2.PdfFileMerger(strict=True)

pdfFile = writer.addBookmark(
    title="new bookmark",
    pagenum=2,
)

print(pdfFile)
