import pandas as pd
import numpy as np

# Set the display option to show all floats in standard decimal format
pd.options.display.float_format = '{:.10f}'.format

cbr = pd.read_csv('CerebrA_LabelDetails.csv')

# cbr.to_clipboard()

label_d = pd.read_csv('label_details.csv')
# label_d.to_clipboard()

result_per_reg = pd.read_csv('results_per_region.csv')
float_columns = result_per_reg.select_dtypes(include=['float']).columns
result_per_reg.to_clipboard(index = False)
# print(result_per_reg)
# print(
    # result_per_reg['sample'].value_counts()
# )

# video1_e = np.load('video1_eLORETA.npy')
# print(video1_e)

# if video1_e.ndim == 2:
    # df = pd.DataFrame(video1_e)
    # df_head_1000 = df.head(1000)
    # df_head_1000.to_clipboard()
    # df.to_excel('video1_e.xlsx')
    # rows, columns = df.shape
    # print(f"Number of rows: {rows}")
    # print(f"Number of columns: {columns}")
# else:
    # print(video1_e)
