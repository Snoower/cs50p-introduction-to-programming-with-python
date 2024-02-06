from fpdf import FPDF

title = "CS50 Shirtificate"

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 50)
        title_width = self.get_string_width(title)
        doc_width = self.w
        self.set_x((doc_width - title_width) / 2)
        self.cell(title_width, 70, title, align="C")

    def shirt(self, name):
        text_width = self.get_string_width(name)
        doc_width = self.w
        self.set_x((doc_width - text_width) / 2)
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        self.cell(text_width, 250, f"{name} took CS50", align="C")

name = input("Name: ")
pdf = PDF(orientation="P", format="A4")
pdf.add_page()
pdf.image("shirtificate.png", 10, 70, 190, keep_aspect_ratio = True)
pdf.shirt(name)
pdf.output("shirtificate.pdf")


#top should says CS50 Shirtificate and centered horizontally
#shirt image should be centered horizontally
#name should be on top of the shirt in white text
