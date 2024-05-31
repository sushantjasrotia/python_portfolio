import pyttsx3
import PyPDF2

pdf_book = open('python.pdf', 'rb')
reading_pdf = PyPDF2.PdfReader(pdf_book)
pdf_pages = len(reading_pdf.pages)

pdf_speaker = pyttsx3.init()
choose_page = reading_pdf.pages[0]
pdf_text = choose_page.extract_text()
pdf_speaker.say(pdf_text)
pdf_speaker.runAndWait()