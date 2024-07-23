import gradio as gr
import pandas as pd
from db_manager import *
from pathlib import Path
from helper_functions import director
from range_calculator import *

path = None
loaded_df = None
collection_name = {0 : 'DataLLRR_Lab1',1 : 'DataLLRR_Lab2'}

data = {
    'Age': [''],
    'Gender': [''],
    'Hemoglobin': [''],
    'Platelet_Count': [''],
    'White_Blood_Cells': [''],
    'Red_Blood_Cells': [''],
    'MCV': [''],
    'MCH': [''],
    'MCHC': ['']
}

def upload_file(filepath,option_pdf):
    
    name = Path(filepath).name
    path = Path(filepath)
    loaded_df = director(str(path))
    if option_pdf != None:
        store_dataframe_to_firestore(loaded_df,collection_name[option_pdf])
    return [gr.UploadButton(visible=False), gr.DownloadButton(label=f"Download {name}", value=filepath, visible=True)]
input_data = pd.DataFrame(data)


def filter_records(input_data,option):
    if option != None :
        store_dataframe_to_firestore(input_data,collection_name[option])
    return input_data

def output_records(option):
    if option != None:
        if option == 0 or option == 1:
            df = get_dataframe_from_firestore(collection_name[option])
        else:
            df1 = get_dataframe_from_firestore(collection_name[0])
            df2 = get_dataframe_from_firestore(collection_name[1])
            df = pd.concat([df1, df2], ignore_index=True)
    txt,image = plotAndFindRanges(df, "output.png")
    return df,txt,image
demo1 = gr.Interface(
    filter_records,
    [
        gr.Dataframe(
            value = input_data,
        ),
        gr.Dropdown(["Lab 01", "Lab 02"], type="index",label = "Choose Lab",container = True,info = 'select'),
    ],
    "dataframe",
    description="Enter Data",
)

with gr.Blocks() as demo2:
    gr.Markdown("Upload Input PDF File")
    with gr.Row():
        u = gr.UploadButton("Upload Input Printed Results(PDF File)",file_count = "single")
        option_pdf = gr.Dropdown(["Lab 01", "Lab 02"], type="index",label = "Choose Lab",container = True,info = 'select')
    u.upload(upload_file,[u,option_pdf])

demo3 = gr.Interface(
    output_records,
    [
        gr.Dropdown(["Lab 01 Local Ranges", "Lab 02 Local Ranges","Global Ranges"], type="index",label = "Choose Lab",container = True,info = 'select')
    ],
    ["dataframe","text","image"],
    description="Click Generate to View Database",
)


demo = gr.TabbedInterface([demo1,demo2,demo3],["Manual Entry","PDF Upload","Database"])
demo.launch()