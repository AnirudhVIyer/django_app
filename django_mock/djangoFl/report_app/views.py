from django.shortcuts import render

# Create your views here.
# Create your models here.
from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas

def generate_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    p.drawString(100, 100, "Hello, world. This is a PDF report.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    return response


def report_page(request):
    print('check')
    return render(request, 'report_download.html')