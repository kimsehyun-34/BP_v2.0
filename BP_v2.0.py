import pandas as pd

fi = pd.read_csv('test.csv')

num_of_cases = fi.groupby('Classe')['rv'].max()
n_top = num_of_cases.nlargest(10).index

from benfordslaw import benfordslaw
def benford(classe, pos):
    global fi
    fi_n = fi[fi.Classe == classe]
    data = fi_n['basic']
    bl = benfordslaw(alpha=0.05, method='ks', pos=pos, verbose=3)
    results = bl.fit(data) # 분석
    bl.plot(title=classe+ ', pos: '+str(pos)) #출력

for classe in n_top:
    benford(classe, 1)
