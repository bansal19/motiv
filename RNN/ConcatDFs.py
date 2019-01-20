import pandas as pd

happy_df = pd.read_csv("lowqualhappy.csv")
sad_df = pd.read_csv("lowqualsad.csv")
dreamy_df = pd.read_csv("lowqualdreamy.csv")

happy_and_sad_df = pd.concat([happy_df, sad_df], ignore_index=True)
all_df = pd.concat([happy_and_sad_df, dreamy_df], ignore_index=True)

all_df.to_csv("lowqualall.csv")
print(all_df)
