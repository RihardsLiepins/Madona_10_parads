import csv

def lasi_csv(filename, column_number):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > column_number:
                    print(row[column_number])
                else:
                    print("Nav visi vārda viena kolluna.")
    except FileNotFoundError:
        print(f"Fails '{filename}' nav atrasts.")
    except Exception as e:
        print(f"Ir notikusi kļūda: {e}")

lasi_csv("pd.csv", 3)  
