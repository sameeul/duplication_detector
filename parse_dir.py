import argparse
import operator

#set up command line processing
parser = argparse.ArgumentParser(description = "Find duplication in a directory")
parser.add_argument("--name", required = True, type = str, help = "Text file containing file listing")
args = parser. parse_args()
input_file_name=args.name

# now work on finding duplicates

file_dict = {}
status_code = {"release":2, "review":3, "in-process":5}

with open(input_file_name) as fp:
    for line in fp:
        line = line.strip()     
        file_name_data = line.split("\\")

        if len(file_name_data) == 3:
            file_name = file_name_data[-1].lower()
            status = file_name_data[1].lower()
            if status in status_code:
                if file_name in file_dict:
                    file_dict[file_name] = file_dict[file_name]*status_code[status]
                else:
                    file_dict[file_name] = status_code[status]

#processing done, now print
                
file_in_two_dir = []
file_in_three_dir = []

for file_name in file_dict:
    if file_dict[file_name] > 5 and file_dict[file_name] < 30:
        file_in_two_dir.append(file_name)
    if file_dict[file_name] == 30:
        file_in_three_dir.append(file_name)

print("Total %d files are unique"%(len(file_dict)-len(file_in_two_dir)-len(file_in_three_dir)))    
print("Total %d files are duplicate across two directories"%(len(file_in_two_dir)))
print("Total %d files are duplicate across three directories"%(len(file_in_three_dir)))
print("Total %d files are duplicate"%(len(file_in_two_dir)+len(file_in_three_dir)))

duplicate_files = file_in_two_dir+file_in_three_dir
if len(duplicate_files) != 0:
    duplicate_files.sort()

    print("\nList of duplicate files:\n")
    print("Review | Release | In-Process | Filename")
    print("----------------------------------------")
    
    for file_name in duplicate_files:
        line = ""
        if file_dict[file_name] % status_code["review"] == 0:
            line = line + "   X    "
        else:
            line = line + "        "

        if file_dict[file_name] % status_code["release"] == 0:
            line = line + "    X     "
        else:
            line = line + "          "

        if file_dict[file_name] % status_code["in-process"] == 0:
            line = line + "     X       "
        else:
            line = line + "             "

        line = line+file_name
        print(line)

#list top 10 duplication series
#optional
series_dict = {}
for file in duplicate_files:
    file_comp = file.split("-")
    series_start_code = file_comp[0]
    if len(file_comp) > 2:
        if series_start_code in series_dict:
            series_dict[series_start_code] = series_dict[series_start_code]+1
        else:
            series_dict[series_start_code] = 1
sorted_series_list = sorted(series_dict.items(), key=operator.itemgetter(1), reverse=True)
print("\nMost Duplicated Series:\n")
print("Series Code        Number of Duplicates")
print("------------------------------------------")
for data in sorted_series_list[0:10]:
    print("%s                %d"%(data[0], data[1]))
        
        
