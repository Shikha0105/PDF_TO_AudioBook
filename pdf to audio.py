import pyttsx3
import PyPDF2

# path of the PDF file
book = open('lebo116.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(book)

# the page with which you want to start
# this will read the page of 25th page.
page = pdfReader.getPage(10)

# extracting the text from the PDF
text = page.extractText()

# reading the text
speaker = pyttsx3.init()
rate=speaker.getProperty('rate')
speaker.setProperty('rate',250)
speaker.say(text)
speaker.runAndWait()
