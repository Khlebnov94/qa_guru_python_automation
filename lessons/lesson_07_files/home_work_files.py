import os
import csv

from io import BytesIO
from zipfile import ZipFile

from openpyxl import Workbook
from pypdf import PdfReader
from reportlab.pdfgen import canvas


# =========================
# Пути
# =========================

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(CURRENT_DIR, "resources")

os.makedirs(RESOURCES_DIR, exist_ok=True)

pdf_path = os.path.join(RESOURCES_DIR, "home_work_files.pdf")
xlsx_path = os.path.join(RESOURCES_DIR, "home_work_files.xlsx")
csv_path = os.path.join(RESOURCES_DIR, "home_work_files.csv")
zip_path = os.path.join(RESOURCES_DIR, "home_work_files.zip")


# =========================
# Создаём CSV
# =========================

with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])
    writer.writerow(["Alexander", 31])


# =========================
# Создаём XLSX
# =========================

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "name"
sheet["B1"] = "age"

sheet["A2"] = "Alexander"
sheet["B2"] = 31

workbook.save(xlsx_path)


# =========================
# Создаём PDF
# =========================

pdf = canvas.Canvas(pdf_path)

pdf.drawString(100, 750, "QA Guru")
pdf.drawString(100, 730, "Lesson 7")
pdf.drawString(100, 710, "Alexander")

pdf.save()


# =========================
# Создаём ZIP
# =========================

with ZipFile(zip_path, "w") as zip_file:
    zip_file.write(pdf_path, arcname="home_work_files.pdf")
    zip_file.write(xlsx_path, arcname="home_work_files.xlsx")
    zip_file.write(csv_path, arcname="home_work_files.csv")


# =========================
# Проверяем PDF из ZIP
# =========================

def test_pdf_from_zip():
    with ZipFile(zip_path, "r") as zip_file:
        pdf_content = zip_file.read("home_work_files.pdf")

        reader = PdfReader(BytesIO(pdf_content))

        text = reader.pages[0].extract_text()

        print(text)

        assert "QA Guru" in text
        assert "Lesson 7" in text
        assert "Alexander" in text