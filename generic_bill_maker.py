from fpdf import FPDF

class Generic_Bill_Maker(FPDF):
    def __init__(self) -> None:
        """ Initialize the PDF object """
        super().__init__(format='A4', orientation='P')
        self.set_font('Arial', 'B', 16)
        self.set_auto_page_break(True, 0)
        self.set_margins(0, 5, 0)
        self.add_page()
        
        pass

    def header(self) -> None:
        """ Add the header to the PDF """
        self.cell(0, 0.5, "Header", 0, 1, 'C')
        self.ln(20)
        pass

    def footer(self) -> None:
        """ Add the footer to the PDF """
        self.set_y(-15)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", 0, 1, 'C')
        pass

    def add_table(self, table_data: list) -> None:
        """ Add a table to the PDF """
        line_height = self.font_size * 2.5
        col_width = self.epw / len(table_data[0])  # distribute content evenly
        for row in data:
            for datum in row:
                self.multi_cell(col_width, line_height, datum, border=1,
                        new_x="RIGHT", new_y="TOP", max_line_height=self.font_size)
            self.ln(line_height)
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


if "__main__" == __name__:
    """ Run the program """
    bill_maker = Generic_Bill_Maker()
    bill_maker.add_text("Text")
    data = [
        ["First name", "Last name", "Age", "City"],
        ["Jules", "Smith", "34", "San Juan"],
        ["Mary", "Ramos", "45", "Orlando"],
        ["Carlson", "Banks", "19", "Los Angeles"],
        ["Lucas", "Cimon", "31", "Saint-Mahturin-sur-Loire"],
    ]
    bill_maker.add_table(data)
    bill_maker.save_pdf("test.pdf")
    pass
