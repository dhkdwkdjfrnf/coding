start=int(input("시작 값을 입력하세요: "))
end=int(input("끝 값을 입력하세요: "))
baesu=int(input("배수를 입력하세요: "))

def cal_hap(s, e):
    hap=0
    i=s
    while i<=e:
        hap=hap+i
        i=i+1
    return hap

def baesu_sum(s, e, b):
    hap=0
    i=s
    while i<=e:
        if i%b==0:
            hap=hap+i
        i=i+1
    return hap

print(start, "에서", end, "까지의 합은", cal_hap(start, end))
print(start, "에서", end, "까지", baesu, "의 배수의 합은", baesu_sum(start, end, baesu))
