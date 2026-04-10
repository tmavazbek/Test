import json

f = open("markaz.json")

dct = {}

data = json.load(f)
#                    1
# # for branches in data['branches']:
#     print(branches['name'])

#                    2
# # for branches in data['branches']:
#     for teachers in branches['teachers']:
#         if teachers['subject'] == 'Python':
#             print(f"Ism: {teachers['name']}, Branch: {branches['name']}, Tajriba: {teachers['experience']} yil")

#                    3
# for branches in data['branches']:
#     count = 0
#     for students in branches['students']:
#         count+=1
#     dct[branches['name']] = count
# print(dct)


#                   4
# for branch in data['branches']:
#     all = [student for student in branch['students']]
#     natija = max(all, key=lambda x: x['payment'])
# print(f'Eng kop payment: {natija['name']}, Branchi: {branch['name']}')


#                   5
# for branch in data['branches']:
#     natija = sum(student['payment'] for student in branch['students'])
#     print(f'{branch['name']}: {natija}')


#                    6
# for branch in data['branches']:
#     for teacher in branch["teachers"]:
#         if teacher['experience'] > 5:
#             print(f"Ismi: {teacher['name']}, Tajribasi: {teacher['experience']} yil")


#                    7
for branch in data['branches']:
    for teachers in branch['teachers']:
        if teachers['subject'] != 'Python':
            break
    else:
        print(branch['name'])

f.close()