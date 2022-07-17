from fpdf import FPDF
class Generic_Bill_Maker:
    def __init__(self) -> None:
        """ Initialize the PDF object """
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_fill_color(255, 255, 255)
        self.pdf.set_line_width(0.1)
        self.pdf.set_margins(0.5, 0.5, 0.5)
        self.pdf.set_auto_page_break(True, 0.5)

        pass
    def add_header(self, header_text: str) -> None:
        """ Add the header to the PDF """
        self.pdf.set_font("Arial", size=12)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_fill_color(255, 255, 255)
        self.pdf.set_line_width(0.1)
        self.pdf.set_margins(0.5, 0.5, 0.5)
        self.pdf.set_auto_page_break(True, 0.0)
        self.pdf.cell(0, 0.5, header_text, 0, 1, 'C', False)
        pass
    def add_footer(self, footer_text: str) -> None:
        """ Add the footer to the PDF """
        self.pdf.set_font("Arial", size=12)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_fill_color(255, 255, 255)
        self.pdf.set_line_width(0.1)
        self.pdf.set_margins(0.5, 0.5, 0.5)
        self.pdf.set_auto_page_break(True, 0.5)
        self.pdf.cell(0, 0.5, footer_text, 0, 1, 'C', False)
        pass
    def add_table(self, table_data: list) -> None:
        """ Add a table to the PDF """
        self.pdf.set_font("Arial", size=12)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_fill_color(255, 255, 255)
        self.pdf.set_line_width(0.1)
        self.pdf.set_margins(0.5, 0.5, 0.5)
        self.pdf.set_auto_page_break(True, 0.5)
        for row in table_data:
            self.pdf.cell(0, 0.5, row, 0, 1, 'C', False)
        pass
    def add_text(self, text: str) -> None:
        """ Add text to the PDF """
        self.pdf.set_font("Arial", size=12)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_fill_color(255, 255, 255)
        self.pdf.set_line_width(0.1)
        self.pdf.set_margins(0.5, 0.5, 0.5)
        self.pdf.set_auto_page_break(True, 0.5)
        self.pdf.cell(0, 0.5, text, 0, 1, 'C', False)
        pass
    def save_pdf(self, filename: str) -> None:
        """ Save the PDF """
        self.pdf.output(filename)
        pass
if  "__main__" == __name__:
    """ Run the program """
    bill_maker = Generic_Bill_Maker()
    bill_maker.add_header("Header")
    bill_maker.add_footer("Footer")
    bill_maker.add_text("Text")
    bill_maker.add_table(["Row 1", "Row 2", "Row 3"])
    bill_maker.save_pdf("test.pdf")
    pass