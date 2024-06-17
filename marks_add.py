import pandas as pd
df=pd.read_csv('Marks Adding Data.csv')

# Print the dataframe to verify the content
print(df)

rno=df.iloc[:,0]   #extracted the roll nos

# Sum the marks for each roll number
marks_sum = df.groupby(rno)['Marks'].sum().reset_index()

print(marks_sum)

output_file = 'Summarized_Marks.csv'  # Replace with your desired output file path
marks_sum.to_csv(output_file, index=False)

print(f'Summarized marks have been written to {output_file}')
