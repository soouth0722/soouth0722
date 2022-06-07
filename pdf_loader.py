from urllib import request

usr_req = input(r'what is your url? ')

file_url = fr'{usr_req}'

def download_file_information(url):
    fileOpen = request.urlopen(url)
    file_info = fileOpen.read()
    file_info_str = str(file_info)

    file_line = file_info_str.split('\\n')

    newfile = open('file.txt',"w")

    for info in file_line:
        newfile,write(info + '')

    newfile.close()

def download_file_information(file_url)

