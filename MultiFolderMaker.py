#                   CAUTION!          CAUTION!             CAUTION!
#  This program will not successfully complete because ,
#  It will create 26^7(=8031810176) files So it will take 510 years to complete in this laptop
def multi_folder():
    import os
    # path = os.getcwd()
    # print(path)

    # path1="E:\\PROGRAMS\\project\\JARVISYT\\virus01"

    # # foldername='Virus'

    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    def folder_maker(path,i): 
        os.mkdir(path+f"\\{i}")    
        print(f"{i}: {i}  : {path}\{i}")

    for a1 in alphabet:
        path1="E:\\PROGRAMS\\project\\JARVISYT\\virus02"
        # os.mkdir(path+f"\\{i}")       
        # print(f"i: {i}  : {path}\{i}")
        folder_maker(path1,a1)
        
        for a2 in alphabet:
            path2=path1+f"\\{a1}"    #\a
            folder_maker(path2,a2)

            for a3 in alphabet:      
                path3=path2+f"\\{a2}"             
                folder_maker(path3,a3)

                for a4 in alphabet:      
                    path4=path3+f"\\{a3}"             
                    folder_maker(path4,a4)

                    for a5 in alphabet:      
                        path5=path4+f"\\{a4}"             
                        folder_maker(path5,a5)

                        for a6 in alphabet:      
                            path6=path5+f"\\{a5}"             
                            folder_maker(path6,a6)

                            for a7 in alphabet:      
                                path7=path6+f"\\{a6}"             
                                folder_maker(path7,a7)
                
multi_folder()













# alphabet=['A','B','C']
# def mfm(path1):
#     print(f"in func ")
#     for i in alphabet:
#         path1="E:\\PROGRAMS\\project\\JARVISYT\\virus01"
#         os.mkdir(path1+f"\\{i}")
#         path1 = path1 +f"\\{i}"
#         j=0
#         print(f"in for {i}")
#         while(j!=len(alphabet)):
#             print(f"in while {j}")
#             j+=1
#             os.mkdir(path1+f"\\{i}")
#             path1 = path1 +f"\\{i}"
#     return mfm(path1)

# mfm(path1)
















# alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in alphabet:
#     os.mkdir(path +f"\\virus01\\{i}")
#     for j in alphabet :
#         os.mkdir(path +f"\\virus01\\{i}\\{j}")

# def multi_folder(path) :
#     for i in alphabet:
        # if(path=="E:\\PROGRAMS\\project\\JARVISYT\\virus01\\A\\A\\A"):
        #     continue

        # if(path=="E:\\PROGRAMS\\project\\JARVISYT\\virus01\\A\\A\\B"): 
        #     continue
        # if(path=="E:\\PROGRAMS\\project\\JARVISYT\\virus01\\A\\B\\A"):    
        #     continue
        # if(path=="E:\\PROGRAMS\\project\\JARVISYT\\virus01\\A\\B\\B"):
        #     continue
        
#             if(i=='D') :return
#             else:
#                 while(len(alphabet)):
#                     os.mkdir(path +f"\\{i}")    
#                     path = path +f"\\{i}"
#                     # print(f"path is   : {path} ")
#                 return multi_folder(path)
    
# multi_folder(path1)
