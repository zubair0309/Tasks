file=open("demo.txt1",mode='a')
write_data=file.write("\n sorry bro its enough to talk...")
file.close()

file1=open("demo.txt1",mode='r')
read_data=file1.read()
print(read_data)
file1.close()

file2=open("demo.txt1",mode='w')
write_data=file2.write("\n life is unpredictable just move on.....")
print(write_data)
file2.close()

file3=open("demo.txt1",mode='a+')
append_data=file3.write("\nnothing is impossible when we keep practicing....")
print(append_data)
file3.close()

file4=open("demo.txt1",mode='r+')
read1_data=file4.read()
print(read1_data)
file4.close()

file5=open("demo.txt1",mode='w+')
write1_data=file5.write("\n life is about winning and loosing......")
file5.close()

