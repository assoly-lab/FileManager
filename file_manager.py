import os
import shutil

working_directory = "Directory path here!"
os.chdir(working_directory)
try :
    for file in os.listdir():
        file_name,file_extension = os.path.splitext(file)
        print(file_name,file_extension)
        if not file_extension :
            pass
        elif file_extension in (".zip",".rar"):
            os.mkdir("Compressed")
            shutil.move(os.path.join(working_directory,f"{file_name}{file_extension}"),os.path.join(working_directory,"Compressed",f"{file_name}{file_extension}"))
        elif file_extension in (".exe",".msi"):
            os.mkdir("Installers")
            shutil.move(os.path.join(working_directory,f"{file_name}{file_extension}"),os.path.join(working_directory,"Installers",f"{file_name}{file_extension}"))  
        elif file_extension in (".pdf",".txt",".xlsx",".docx",".pptx",".doc"):
            os.mkdir("Documents")
            shutil.move(os.path.join(working_directory,f"{file_name}{file_extension}"),os.path.join(working_directory,"Documents",file_name+file_extension))   
        elif file_extension in (".mp3",".wav",):
            os.mkdir("Music")
            shutil.move(os.path.join(working_directory,f"{file_name}{file_extension}"),os.path.join(working_directory,"Music",f"{file_name}{file_extension}"))       
        elif file_extension in (".jpeg",".jpg",".PNG"):
            os.mkdir("Images")
            shutil.move(os.path.join(working_directory,f"{file_name}{file_extension}"),os.path.join(working_directory,"Images",f"{file_name}{file_extension}"))
        else :
            shutil.move(os.path.join(working_directory,f"{file_name}{file_extension}"),os.path.join(working_directory,"Other Files",f"{file_name}{file_extension}"))
except (FileNotFoundError,PermissionError,FileExistsError) :
    pass


        