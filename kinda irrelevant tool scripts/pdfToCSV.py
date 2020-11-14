import tabula

df = tabula.read_pdf("registry.pdf", encoding='utf-8', spreadsheet=True, pages='all')


#print(df)
tabula.convert_into("registry.pdf", "registry.csv", output_format="csv", pages='all')