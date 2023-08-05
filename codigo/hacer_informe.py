import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys

# Function to generate the report
def generate_report(report_number, diff_df):
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')

    if diff_df.shape[0] == 0:
        print("La lista vieja y la nueva son iguales")
        sys.exit()

    the_table = ax.table(cellText=diff_df.values, colLabels=diff_df.columns, loc='center')
    pdf_path = os.path.join("reports", f"informe{report_number}.pdf")  # Save report in the 'reports' folder
    pp = PdfPages(pdf_path)
    pp.savefig(fig, bbox_inches='tight')
    pp.close()

    print("Informe generado exitosamente. Hay", diff_df.shape[0], "precios para cambiar")

# Read in the two CSV files
df1 = pd.read_csv("../lista_bacha.csv")
df2 = pd.read_csv("../lista_vieja.csv")

# Merge the two dataframes based on the "id" column
merged_df = pd.merge(df1, df2, on="id_bacha", suffixes=["_old", "_new"])

# Filter the merged dataframe to only include rows where the "precio_bacha" values are different
diff = merged_df[merged_df["precio_bacha_old"] != merged_df["precio_bacha_new"]]

# Filter and rename
diff_f = diff[["id_bacha", "name_bacha_new", "precio_bacha_new", "precio_bacha_old"]]
diff_df = diff_f.rename(columns={"name_bacha_new": "Nombre actualizado", "precio_bacha_old": "Precio nuevo",
                                 "precio_bacha_new": "Precio viejo"})

# Check if the 'reports' directory exists, if not, create it
if not os.path.exists("reports"):
    os.makedirs("reports")

# Find the highest report number in the directory
existing_reports = [f for f in os.listdir("reports") if f.startswith("informe")]
report_numbers = [int(f.split(".")[0][len("informe"):]) for f in existing_reports]
if report_numbers:
    highest_report_number = max(report_numbers)
else:
    highest_report_number = 0

# Generate a new report with an incremented report number
new_report_number = highest_report_number + 1
generate_report(new_report_number, diff_df)

print(f"New report generated: informe{new_report_number}.pdf")
