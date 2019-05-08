counter = 0

with open(r'C:\Users\dell\Desktop\text-file-process-shiancuc\text-file-process\log_files\201811123007.log',encoding='utf8') as f:
    for line in f:
        student_id = line.split(',')[1]
        #print(student_id)
        id = student_id.split('：')[1]
        print(id)
        if id == '201811123007':
            counter = counter + 1

print('201811123007打卡次数：',end='')
print(counter)