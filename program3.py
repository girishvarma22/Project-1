import csv
import sys

def csv_column_sum(file_path, columns):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)

            # Validate columns
            for col in columns:
                if col not in header:
                    raise ValueError(f"Column '{col}' not found in the CSV file.")

            # Initialize column sums
            col_sums = {col: 0 for col in columns}

            # Sum the specified columns
            for row in reader:
                for col in columns:
                    col_index = header.index(col)
                    col_sums[col] += float(row[col_index])

            return col_sums

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <csv_file> <column1> [<column2> ...]")
        sys.exit(1)

    csv_file = sys.argv[1]
    columns_to_sum = sys.argv[2:]

    result = csv_column_sum(csv_file, columns_to_sum)

    print("Column Sums:")
    for col, total in result.items():
        print(f"{col}: {total}")
