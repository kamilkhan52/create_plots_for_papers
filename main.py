import pandas as pd
import matplotlib.pyplot as plt

font_size = 14
params = {'legend.fontsize': font_size,
          'figure.figsize': (10, 5),
          'axes.labelsize': font_size,
          'axes.titlesize': font_size,
          'xtick.labelsize': font_size,
          'ytick.labelsize': font_size,
          'axes.grid': True,
          'grid.alpha': 0.70}
plt.rcParams.update(params)

plt.rc('axes', axisbelow=True)
graphs_dir = "C:\\Users\\Kamil\\PycharmProjects\\matplot\\Graphs"

# Latency
excel_file = "8_apps_results.xlsx"
sheet_name = "final latency graph"

plot_data = pd.read_excel("\\".join([graphs_dir, excel_file]), sheet_name=sheet_name)
# plot_data.drop(plot_data.columns[plot_data.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
plot_data.plot(kind='bar', x=plot_data.columns[0], y=plot_data.columns[1:6], color=['#5B9BD5', '#ED7D31', '#A5A5A5', '#3660AC', '#FFC000'],
               ylim=[0.40, 1.75], xlabel='', ylabel='Normalized Avg. Latency', fontsize=font_size, width=0.65)
plt.legend(ncol=len(plot_data.columns[1:6]), loc='upper center', fontsize=font_size)  # , bbox_to_anchor=(0.5, 1.1)
plt.grid(axis='x')
plt.savefig("avg_latency.png", bbox_inches='tight')
# plt.show()

# Falsefull
excel_file = "8_apps_results.xlsx"
sheet_name = "final falsefull graph"

plot_data = pd.read_excel("\\".join([graphs_dir, excel_file]), sheet_name=sheet_name)
plot_data.plot(kind='bar', x=plot_data.columns[0], y=plot_data.columns[2:5], color=['#ED7D31', '#A5A5A5', '#3660AC'],
               ylim=[4, 15.5], xlabel='', ylabel='Avg. Falsefull Rate', fontsize=font_size, width=0.65)
plt.legend(ncol=len(plot_data.columns[1:6]), loc='upper center', fontsize=font_size)  # , bbox_to_anchor=(0.5, 1.1)
plt.grid(axis='x')
plt.savefig("avg_falseful.png", bbox_inches='tight')
# plt.show()

# Unique RMC configurations
excel_file = "8_apps_results.xlsx"
sheet_name = "final allocation summary graph"

plot_data = pd.read_excel("\\".join([graphs_dir, excel_file]), sheet_name=sheet_name)
plot_data.plot(kind='bar', x=plot_data.columns[0], y=plot_data.columns[1:4], color=['#ED7D31', '#A5A5A5', '#3660AC'],
               ylim=[0, 1], ylabel='Frequency', xlabel='', fontsize=font_size, width=0.65, stacked=True)
plt.legend(loc='upper center', fontsize=font_size, bbox_to_anchor=(0.5, 1.32))  # , bbox_to_anchor=(0.5, 1.1)
plt.grid(axis='x')
plt.savefig("allocation_summary.png", bbox_inches='tight')
# plt.show()

# Energy Consumption
excel_file = "8_apps_results.xlsx"
sheet_name = "final energy graph"

plot_data = pd.read_excel("\\".join([graphs_dir, excel_file]), sheet_name=sheet_name)
plot_data.plot(kind='bar', x=plot_data.columns[0], y=plot_data.columns[1:5], color=['#5B9BD5', '#ED7D31', '#A5A5A5', '#3660AC', '#FFC000'],
               ylim=[0.4, 1.75], xlabel='', ylabel='Normalized Energy', fontsize=font_size, width=0.65)
plt.legend(ncol=len(plot_data.columns[1:5]), loc='upper center', fontsize=font_size)  # , bbox_to_anchor=(0.5, 1.1)
plt.grid(axis='x')
plt.savefig("energy.png", bbox_inches='tight')
# plt.show()

# scalability
excel_file = "8_apps_results.xlsx"
sheet_name = "final scalability graph"

plot_data = pd.read_excel("\\".join([graphs_dir, excel_file]), sheet_name=sheet_name)
plot_data.plot(kind='bar', x=plot_data.columns[0], y=plot_data.columns[1:5], color=['#5B9BD5', '#ED7D31', '#A5A5A5', '#3660AC', '#FFC000'],
               ylim=[0, 2.70], xlabel='', ylabel='Normalized Avg. Latency', fontsize=font_size, width=0.65)
plt.legend(ncol=len(plot_data.columns[1:5]), loc='upper center', fontsize=font_size)  # , bbox_to_anchor=(0.5, 1.1)
plt.grid(axis='x')
plt.xticks(rotation=0)
plt.savefig("scalability.png", bbox_inches='tight')
plt.show()
