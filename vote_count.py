# data = {}
# with open('2021-09-14_party distribution_1_st_2021.csv', 'r', encoding = 'UTF-8') as infile:
#     header = infile.readline().strip().split(';')
#     # print(header)
#     for lines in infile:
#         _, Fylkenavn, _, _, _, _, Partikode, _, _, _, _, _, Antall_stemmer_totalt, _, _, _, _, _ = lines.split(';')
#         data[Partikode] = data.get(Partikode, 0) + int(Antall_stemmer_totalt)
#
# data2 = dict.fromkeys(data)
# for key, value in data.items():
#     data2[key] = value/sum(data.values())
# # print(data.items())
# # print(data2.items())
#
# data3 = {}
# for dupe_key in set(data) & set(data2):
#     data3[dupe_key] = [data[dupe_key], data2[dupe_key]]
# print(data3)
#
# print("{:<15} {:<15} {:<10}".format('Partikode', 'Total_vote', 'Percentage'))
# for k, v in sorted(data3.items(), key=lambda s: s[1], reverse=True):
#     Total_vote, Percentage = v
#     if Percentage >= 0.04:
#         print("{:<15} {:<15} {:.2f}".format(k, Total_vote, Percentage))
#
# # print(data3['V'])
# # print(data3['MDG'])
# # print(data3['KRF'])

def Count_vote(filename, Number = 0):
    data = {}
    with open(filename, 'r', encoding='UTF-8') as infile:
        header = infile.readline().strip().split(';')
        # print(header)
        for lines in infile:
            _, Fylkenavn, _, _, _, _, Partikode, _, _, _, _, _, Antall_stemmer_totalt, _, _, _, _, _ = lines.split(';')
            data[Partikode] = data.get(Partikode, 0) + int(Antall_stemmer_totalt)

    data2 = dict.fromkeys(data)
    for key, value in data.items():
        data2[key] = value / sum(data.values()) *100

    data3 = {}
    for dupe_key in set(data) & set(data2):
        data3[dupe_key] = [data[dupe_key], data2[dupe_key]]

    print("{:<15} {:<15} {:<10}".format('Partikode', 'Total_vote', 'Percentage'))
    for k, v in sorted(data3.items(), key=lambda s: s[1], reverse=True):
        Total_vote, Percentage = v
        if Percentage > Number:
            print("{:<15} {:<15} {:.2f}".format(k, Total_vote, Percentage))

Count_vote('2021-09-14_party distribution_1_st_2021.csv', 4)
