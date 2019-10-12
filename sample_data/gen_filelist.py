import os
import matplotlib.image as mpimg
input_path = "sample_data/identity/input"

if __name__ == "__main__":
    file_name_list = os.listdir(input_path)
    file_name_list = [file_name for file_name in file_name_list if os.path.isfile(input_path + '/' + file_name)]

    new_file_name_list = []
    for file_name in file_name_list:
        if mpimg.imread("sample_data/identity/input/" + file_name).shape != mpimg.imread(
                "sample_data/identity/output/" + file_name).shape:
            print(file_name)
        else:
            new_file_name_list.append(file_name)
    
    with open("sample_data/identity/filelist.txt", 'w') as f:
        f.write("\n".join(new_file_name_list))
