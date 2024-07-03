# from data_preprocessing import data_preprocess
import pandas as pd
import plotly.express as px
# from IPython.display import Image
import warnings
warnings.filterwarnings("ignore")
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

import plotly.io as pio
# import io
# from PIL import Image
import string
# a =[]

def data_visualization():

    data = pd.read_csv('./Kaggle_Test_Dataset_v2.csv')
    #plt.figure(figsize=(10,8))
    #sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    #plt.show()
    count = 0
    letters = list(string.ascii_lowercase)
    names_cat=["deck_risk","ppap_risk","stop_auto_buy","went_on_backorder"]
    for i in names_cat:
        count+=1
        lst = []
        lst.append(i)
        df = data.groupby(by=lst).size().reset_index(name="counts")
        fig=px.bar(data_frame=df, x=i, y="counts",color=i)
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "black")
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        fig.write_image(f"count_{i}.jpg")
        # a.append(fig)
        #img_bytes = fig.to_image(format="png")
        #f2 = go.FigureWidget(fig)
        # fig.write_image(f"{i}.pdf")
        # img_bytes = fig.to_image(format="png")
        # Image(img_bytes)
    
    names=["national_inv","sales_1_month", "sales_9_month", "min_bank", "perf_6_month_avg","perf_12_month_avg", "local_bo_qty"]

    for j in names:
        count += 1
        fig = px.box(data, y=j)
        fig.update_layout(template='plotly_dark')
        # fig.update_layout(plot_bgcolor = "black")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        fig.write_image(f"box_{j}.jpg")
        # a.append(fig)
    #for i in names:
    #    plt.figure(figsize=(5,5))
    #    plt.bar(data["went_on_backorder"],data[i])
    #    plt.ylabel(i)
    #    plt.xlabel("went_on_backorder")
    #    plt.title(i)
    #plt.show()



    # figures = a
    # image_list = [pio.to_image(fig, format='png', width=1440, height=900, scale=1.5) for fig in figures]
    # for index, image in enumerate(image_list):
    #     with io.BytesIO() as tmp:
    #         tmp.write(image)  # write the image bytes to the io.BytesIO() temporary object
    #         image = Image.open(tmp).convert('RGB')  # convert and overwrite 'image' to prevent creating a new variable
    #         image_list[index] = image  # overwrite byte image data in list, replace with PIL converted image data

    # # pop first item from image_list, use that to access .save(). Then refer back to image_list to append the rest
    # image_list.pop(0).save(r'./STudent#583.pdf', 'PDF',
    #                     save_all=True, append_images=image_list, resolution=100.0)  # TODO improve resolution

    
    return data



data_visualization()
