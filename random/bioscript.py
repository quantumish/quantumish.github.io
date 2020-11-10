import csv
import sys

def get_range(path, xrow, yrow, bound_lower, bound_upper, outpath):
    f = open(outpath, "w")
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for num, row in enumerate(reader):
            if num == 0: continue
            contents = row[0].split(",")
            if contents[xrow] == '' or contents[yrow] == '': continue
            coords = (float(contents[xrow]), float(contents[yrow]))
            if coords > bound_lower and coords < bound_upper:
                f.write(', '.join(row) + '\n')
    f.close()

get_range(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), (int(sys.argv[6]),int(sys.argv[7])), sys.argv[8])
