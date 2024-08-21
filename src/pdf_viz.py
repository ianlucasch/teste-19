import os
import camelot
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

file_name = "Redrex - Fatura (1)"
path = os.path.abspath(f"src/files/pdf/redrex/{file_name}.pdf")

tables = camelot.read_pdf(
    path,
    pages="1-end",
    flavor="stream",
    table_areas=["65, 568, 500, 298"],
    columns=["65, 107, 156, 212, 280, 336, 383, 450"],
    strip_text=" .\n"
)

print(tables[0].parsing_report)

# camelot.plot(tables[0], kind="contour")

# plt.show()

print(tables[0].df)

print("Pause")