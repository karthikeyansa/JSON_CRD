from mypythonlib.myfunctions import JSONCRD

file_path = input("Enter file_path: ")
output_file = input("Enter file_name: ")

if len(file_path)>0 and len(output_file)>0:
    obj = JSONCRD(file_path= file_path,output_file= output_file)
elif len(file_path)== 0 and len(output_file)>0:
    obj = JSONCRD(output_file=output_file)
elif len(file_path) == 0 and len(output_file) ==0:
    obj = JSONCRD()

print("creating...")
print(obj.create_data())
print("reading...")
print(obj.read_data())
print("deleting...")
print(obj.delete_data())