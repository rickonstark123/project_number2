from ast import If
from proj_data import Datanumber
#class acx:
def main():
    p_number = input()
    sum = 0
    sum_percent = 0
    double_num = []
    mean_duo_bf = []
    mean_duo_af = []
    category = []
    category_test = []
    while not(p_number.isnumeric()) or not(len(p_number) == 10):
        print("Please Enter numeric only and full number.")
        p_number = input()
    for i in p_number:
        sum += int(i)
    data = Datanumber.number_phone()
    mean_num = data['txt_detail'][sum]
    for k in range(8):
        duo = p_number[k + 1] + p_number[k + 2]
        double_num.append(duo)
        category_first = data['category'][int(duo)]
        category_first = category_first.split()
        for z in category_first:
            if z not in category or z != 'ไม่มี':
                category_test.append(z)
        for g in category_test:
            if g not in category and g != 'ไม่มี':
                category.append(g)
        mean_num_duo = data['txt_shot'][int(duo)]
        mean_duo_bf.append(mean_num_duo)
        sum_percent += data['percent'][int(duo)] #ผลรวมเปอร์เซ็นของแต่ละคู่เลข
    sum_percent //= 0.08
    for a in range(8):
        txt_duo = mean_duo_bf[a]
        mean_duo_af.append(txt_duo)
    print(sum, mean_num, int(sum_percent), 100 - int(sum_percent), double_num, mean_duo_af, list(category))
main()
#sum_1 = ผลรวมเลข
#mean_num = ผลดี
#100 - percent_num = ผลเสีย
#double_num = คู่เลข
#mena_duo_list = ความหมายแต่ละคู่เลข
#category = ประเภทดวงเด่นๆของเบอร์นั้นๆ
    

