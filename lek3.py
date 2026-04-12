#khi so sánh 2 chuỗi kí tự, so sánh lần lượt từng phần tử từ trái sang phải, khi gặp phần tử khác biệt, lập tức so sánh và kết luận mà không cần quan tâm những phần tử khác
##tương tự với list và các loại biến khác
#b <<= a 
# b * 10 mũ a
#print(4**2)
a = int(float(input()))
if a - int(a)< 0.5:
    print(a)
else:
    print(a+1)


#def
def tinhhinhchunhat(a,b):
    chuvi=2*(a+b)
    dientich=a*b
    return chuvi, dientich
a,b = map(int, input().split())
chuvi, dientich = tinhhinhchunhat(a,b)
print(f"{chuvi} {dientich}")