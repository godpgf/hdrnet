import os
input_path = "sample_data/identity/low"

if __name__ == "__main__":
    file_name_list = os.listdir(input_path)
    file_name_list = [file_name for file_name in file_name_list if os.path.isfile(input_path + '/' + file_name)]
    with open("sample_data/identity/filelist.txt", 'w') as f:
        f.write("\n".join(file_name_list))
