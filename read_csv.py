import pandas as pd
from matplotlib import pyplot as plt
pf = pd.read_csv('data/survey_results_public.csv')
pf_short = pf.head(9)

# print('This is column selection')
# print('========================================================')

# # this is for selection collumns from data
# print(pf['Student'])
# print(pf.Country)

# print('----------------------------------------------------------')

# print('This is row selection')
# print('===========================================================')

# #this is for row selection
# students = pf[pf.Student == 'Yes, full-time']
# Youngsters = pf[pf.Age < 20]
# print(students)
# print(Youngsters)

# print('----------------------------------------------------------')
# print('===================================')
# print('=====================================')
# print('=====================================')


# Data visualizing with matplotlib
print(plt.style.available)
plt.style.use('ggplot')
plt.plot(pf_short.Respondent, pf_short.Age, label="developers",
		color="Olive", marker="d", linewidth=2, linestyle="-.")

plt.title('Ages of Developers')
plt.xlabel('Respondents')
plt.ylabel('Age')
plt.text(5, 20, 'Only 9 developers here')
plt.legend()

plt.show()
