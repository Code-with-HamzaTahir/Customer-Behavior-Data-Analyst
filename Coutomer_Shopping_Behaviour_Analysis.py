import pandas as pd 

df = pd.read_csv('C:\\Users\\Asus Zephyrus RTX\\Downloads\\customer_shopping_behavior.csv')

df.info()

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

df['Review rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

print(df.isnull().sum())

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df.columns = df.columns.str.replace('purchase_amount_(usd)','puchased_amount')
print(df.columns)


labels = ('Young_adult', 'Adult', 'middle_aged', 'senior')
df['age_group'] = pd.qcut(df.age, q=4, labels=labels)
print(df[['age','age_group']].head(10))

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
print(df[['purchase_frequency_days', 'frequency_of_purchases']].head(10))


df.drop('promo_code_used', axis=1)

print(df.columns)

from sqlalchemy import create_engine

username = "postgres"
password = "hamzah@@@@@"  
host = "localhost"   
port = "5432" 
database = "Customer_Behavior"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@127.0.0.1:{port}/{database}"
)

table_name = "customer"   # choose any table name
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")