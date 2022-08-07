import pandas as pd

fil=input("파일이름 입력(확장자.csv 입력): ")
df = pd.read_csv(fil)
n=input("분류기준(ex: 나라, 지역, 종목...) \n(자료가 다수일시 사용): ")
b=input("도표정리 기준항목(입력한 항목을 기준으로 도표가 생성됨): ")

num_of_cases = df.groupby(n)[b].max()
n_top = num_of_cases.nlargest(10).index

from benfordslaw import benfordslaw
def benford(cj, pos):
    global df
    df_n = df[df.co == cj]
    data = df_n['basic']
    bl = benfordslaw(alpha=0.05, method='ks', pos=pos, verbose=3)
    results = bl.fit(data) # 분석
    bl.plot(title=cj+ ', pos: '+str(pos)) #출력

for cj in n_top:
    benford(cj, 1)