from PIL import Image
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plotAndFindRanges(df, output_path):
    # Drop non-numerical columns from the original DataFrame
    df = df.drop(columns=['Age', 'Gender'])

    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Try converting the column to numeric type
        try:
            df[column] = pd.to_numeric(df[column])
        except ValueError:
            # If conversion fails (e.g., if the column contains non-numeric values),
            # leave the column as it is
            pass
    # Assuming 'df' is your DataFrame
    # First, calculate the IQR for each column
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1

    # Identify outliers for each column using the IQR method
    #outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))

    # Visualize the distribution of each column with box plots, marking outliers
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, orient="h", fliersize=5)
    plt.title("Boxplot of Clincal Parameters (Outliers removal and range determination using IQR)")
    plt.xlabel("Values")
    plt.ylabel("Columns")

    # Determine the resulting range for each column after removing outliers
    range_without_outliers = {}
    for column in df.columns:
        lower_bound = Q1[column] - 1.5 * IQR[column]
        upper_bound = Q3[column] + 1.5 * IQR[column]
        column_values = df[column][(df[column] >= lower_bound) & (df[column] <= upper_bound)]
        range_without_outliers[column] = (column_values.min(), column_values.max())
        # Annotate the plot with resulting range after removing outliers
        plt.text(upper_bound, df.columns.get_loc(column), f'Range: {range_without_outliers[column]}',
                 verticalalignment='center')
    output_txt = "Resulting range for each column after removing outliers:"
    for column, value_range in range_without_outliers.items():
        output_txt += f"{column}: {value_range}\n" 
    plt.savefig(output_path)

    # Replace 'image.jpg' with the path to your image file
    image = Image.open(output_path)
    return output_txt,image

