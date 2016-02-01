# BMI值計算公式:   BMI = 體重(公斤) / 身高*身高(公尺*公尺)
# 例如：一個52公斤的人，身高是155公分，則BMI為 :
# 52(公斤)/1.55*1.55 ( 公尺*公尺 )= 21.6
# 體重正常範圍為  BMI=18.5～24
height = 1.75
weight = 80.5
bmi = weight/(height*height)

if bmi < 18.5:
    print('过轻')
# elif bmi >= 18.5 and bmi < 25:
elif 18.5 <= bmi < 25:
    print('正常')
# elif bmi >= 25 and bmi < 28:
elif 25 <= bmi < 28:
    print('过重')
# elif bmi >= 28 and bmi < 32:
elif 28 <= bmi < 32:
    print('肥胖')
elif bmi > 32:
    print('严重肥胖')
else:
    print('Exception !')
