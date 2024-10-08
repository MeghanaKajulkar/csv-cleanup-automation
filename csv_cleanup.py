import csv

def clean_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write only non-empty rows to the output file
        for row in reader:
            if any(row):  # Checks if the row has any non-empty values
                writer.writerow(row)

    print(f"CSV cleaned and saved to {output_file}")

# Jenkins will trigger this script
if __name__ == "__main__":
    input_file = 'dirty_data.csv'    # Input CSV file
    output_file = 'cleaned_data.csv'  # Output CSV file
    clean_csv(input_file, output_file)
