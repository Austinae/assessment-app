import numpy as np
import matplotlib.pyplot as plt

resultperstudent = {'user23': 100.0, 'papaaa': 50.0, 'williamau': 25.0, 'Katapult': 100.0}
highest_name = (','.join(str(key) for min_value in (max(resultperstudent.values()),) for key in resultperstudent if resultperstudent[key] == min_value)).split(',')
lowest_name = (','.join(str(key) for min_value in (min(resultperstudent.values()),) for key in resultperstudent if resultperstudent[key] == min_value)).split(',')
mark_max = max(resultperstudent.keys(), key=(lambda k: resultperstudent[k]))
mark_min = min(resultperstudent.keys(), key=(lambda k: resultperstudent[k]))
listt = [highest_name, resultperstudent[mark_max], lowest_name, resultperstudent[mark_min]]


plt.rcdefaults()

objects = ('Average', str(highest_name), str(lowest_name))
y_pos = np.arange(len(objects))
performance = [75.6, resultperstudent[mark_max], resultperstudent[mark_min]]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Marks')
plt.title('Programming language usage')

plt.show()