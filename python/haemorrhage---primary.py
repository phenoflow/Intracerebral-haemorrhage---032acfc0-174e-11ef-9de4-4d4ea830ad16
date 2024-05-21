# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"G61..00","system":"readv2"},{"code":"3535.0","system":"readv2"},{"code":"40338.0","system":"readv2"},{"code":"19201.0","system":"readv2"},{"code":"28314.0","system":"readv2"},{"code":"13564.0","system":"readv2"},{"code":"7912.0","system":"readv2"},{"code":"62342.0","system":"readv2"},{"code":"107440.0","system":"readv2"},{"code":"31060.0","system":"readv2"},{"code":"7017.0","system":"readv2"},{"code":"96630.0","system":"readv2"},{"code":"53810.0","system":"readv2"},{"code":"6960.0","system":"readv2"},{"code":"5051.0","system":"readv2"},{"code":"30045.0","system":"readv2"},{"code":"31595.0","system":"readv2"},{"code":"18604.0","system":"readv2"},{"code":"30202.0","system":"readv2"},{"code":"57315.0","system":"readv2"},{"code":"46316.0","system":"readv2"},{"code":"I61","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('intracerebral-haemorrhage-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["haemorrhage---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["haemorrhage---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["haemorrhage---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
