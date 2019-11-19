input_file_name="nas_top_level_dir.txt"

file_dict = {}
status_code = {"release":2, "review":3, "in-process":5}

with open(input_file_name) as fp:
    for line in fp:
        line = line.strip()     
        file_name_data = line.split("\\")

        if len(file_name_data) > 2:
            file_name = file_name_data[-1].lower()
            status = file_name_data[1].lower()
            if status in status_code:
                if file_name in file_dict:
                    file_dict[file_name] = file_dict[file_name]*status_code[status]
                else:
                    file_dict[file_name] = status_code[status]
                
for key in file_dict:
    if file_dict[key] > 5:
        print("file name %s status %d"%(key, file_dict[key]))
