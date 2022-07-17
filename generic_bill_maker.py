from fpdf import FPDF
class Generic_Bill_Maker(FPDF):
    def __init__(self) -> None:
        """ Initialize the PDF object """
        super().__init__(format='A4', orientation='P')
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.set_auto_page_break(True, 20)
        self.set_margins(0, 0, 0)
        
        pass
    def add_header(self, header_text: str) -> None:
        """ Add the header to the PDF """
        self.cell(0, 0.5, header_text, 0, 1, 'C')
        self.ln(20)
        pass
    def add_footer(self) -> None:
        """ Add the footer to the PDF """
        self.set_y(-15)
        self.cell(0, 0.5, str(self.page_no()), 0, 1, 'C')   
        pass
    def add_table(self, table_data: list) -> None:
        """ Add a table to the PDF """
        for row in table_data:
            self.cell(0, 0.5, row, 0, 1, 'C')
            self.ln(10)
        self.ln()
        pass
    def add_text(self, text: str) -> None:
        """ Add text to the PDF """
        self.cell(0, 0.5, text, 0, 1, 'C')
        self.ln(20)
        pass
    def save_pdf(self, filename: str) -> None:
        """ Save the PDF """
        self.output(filename)
        pass
if  "__main__" == __name__:
    """ Run the program """
    bill_maker = Generic_Bill_Maker()
    bill_maker.add_header("Header")
    bill_maker.add_text("Text")
    bill_maker.add_table(["Row 1", "Row 2", "Row 3"])
    bill_maker.add_footer()
    
    bill_maker.save_pdf("test.pdf")
    pass