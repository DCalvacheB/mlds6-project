! pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip
!pip install dabl

data = pd.read_csv("Train bank.csv", sep="\,")

from pandas_profiling import ProfileReport
  
profile = ProfileReport(data, minimal=True)
profile.to_file(output_file="Bank profiling min.html")

import seaborn as sns
import matplotlib.pyplot as plt

data.corr()[["Subscription"]].sort_values(by="Subscription", ascending=False)
plt.figure(figsize=(8, 12))
heatmap = sns.heatmap(data.corr()[["Subscription"]].sort_values(by="Subscription", ascending=False), vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Correlación de Subscription con las demás variables', fontdict={'fontsize':18}, pad=16);
