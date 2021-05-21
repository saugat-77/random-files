import os 

files=os.listdir()      #directory ko files list garyo
files.remove('managing_external_files.py')
#move files in corresponding folders
def move(folder_name, files):
    for file in files:
        os.replace(file,f'{folder_name}/{file}')

def create_if_not_exist(folder):
    if not os.path.exists(folder):      #tyo thau ma tyo folder cha ki nai bhaera check garcha
        os.makedirs(folder)

create_if_not_exist('Images')   #yo folder haru chaina bhane chai create garcha
create_if_not_exist('Text')
create_if_not_exist('Others')

img_extension=['.jpg','.png','.jpeg']
images=[file for file in files if os.path.splitext(file)[1].lower() in img_extension] 
#img_extension ma bhako format ko file search garcha
#split text ko kaam chai tyo folder lai split garcha ani [0= yesma folder ko name bhayo], [1= folder ko extension]

doc_extension=['.docx', '.txt', '.docs', '.odt']
documents=[file for file in files if os.path.splitext(file)[1].lower() in doc_extension]

# others=[]
# for file in files:
# documents =[file for file in files if os.path.splitext(file)[1].lower() in doc_extension]

others=[]
for file in files:      #mathi ko bhanda farak extension bhako files
    ext=os.path.splitext(file)[1].lower()
    
    if (ext not in img_extension) and (ext not in doc_extension) and os.path.isfile(file):
        others.append(file)

move('Images',images)
move('Text',documents)
move('Others',others)