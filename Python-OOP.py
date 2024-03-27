import pandas as pd

class MarketingDataETL:
    def __init__(self):
        pass

    def extract(self, file_CSV):
        try:
            # Membaca file csv
            df = pd.read_csv(file_CSV, sep=';')
            return df
        except FileNotFoundError:
            print("File anda tidak ditemukan.")
            return None

    def transform(self, data):
        # Melihat struktur dataframe
        print("Struktur DataFrame:")
        print(data)

        # Melihat info dari dataframe
        print("\nInfo DataFrame:")
        print(data.info())

        # Sorting data menurut customer id
        data.sort_values(by='customer_id', inplace=True)

        # Mengecek dan menghilangkan data kosong
        print("\nData missing:")
        print(data.isnull().sum())

        data.dropna(inplace=True)

        # Menghilangkan duplicate baris
        data.drop_duplicates(inplace=True)

        #Mengubah format tanggal
        data['purchase_date'] = pd.to_datetime(data['purchase_date'], format='%d/%m/%y')

        return data

    def store(self, transformed_data, output_file):
        try:
            transformed_data.to_csv(output_file, index=False)
            print("Data yang telah ditransformasi disimpan dalam file '{}'.".format(output_file))
        except Exception as e:
            print("Terjadi kesalahan saat menyimpan data yang diubah:", e)

file_CSV = "marketing_data.csv"
etl = MarketingDataETL()
data = etl.extract(file_CSV)
print("\nData sebelum transformasi:")
print(data)

transformed_data = etl.transform(data)
print("\nData setelah transformasi:")
print(transformed_data)

stored_data = etl.store(transformed_data, "transformed_data.csv")
print(stored_data)



import pandas as pd

class TargetedMarketingETL(MarketingDataETL):
    def _init_(self):
        super()._init_()

    def segment_customers(self, data, criteria):
        segmented_data = data.groupby(criteria)['customer_id'].apply(list)
        return segmented_data
    def transform(self, data):
        transformed_data = super().transform(data)
        criteria = 'product_category'
        segmented_data = self.segment_customers(transformed_data, criteria)
        transformed_data['segmented_customers'] = transformed_data['product_category'].map(segmented_data)

        return transformed_data

targeted_etl = TargetedMarketingETL()

segmented_data = targeted_etl.segment_customers(data, 'product_category')

print("\nHasil Segmentasi Pelanggan:")
for category, customers in segmented_data.items():
    print("Kategori {}: {}".format(category, customers))

file_CSV = "marketing_data.csv"
etl = MarketingDataETL()
data = etl.extract(file_CSV)
print("\nData sebelum transformasi:")
print(data)

transformed_data = etl.transform(data)
print("\nData setelah transformasi:")
print(transformed_data)

targeted_etl = TargetedMarketingETL()
segmented_data = targeted_etl.segment_customers(transformed_data, 'product_category')

print("\nHasil Segmentasi Pelanggan:")
for category, customers in segmented_data.items():
    print("Kategori {}: {}".format(category, customers))

# Memanggil metode transform yang dioverride dalam TargetedMarketingETL
transformed_data_targeted = targeted_etl.transform(data)
print("\nData setelah transformasi dengan segmentasi pelanggan:")
print(transformed_data_targeted)