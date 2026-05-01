import pandas as pd
import matplotlib.pyplot as plt

# 1. تحديد مسار الملف (تأكد من مطابقة المسار في Kaggle)
my_filepath = "../input/fivethirtyeight-comic-characters-dataset/dc-wikia-data.csv"

# 2. تحميل البيانات في المتغير my_data
try:
    my_data = pd.read_csv(my_filepath)
    print("تم تحميل البيانات بنجاح!")
    
    # 3. استعراض أول 5 أسطر من البيانات
    print("\nأول 5 أسطر من البيانات:")
    print(my_data.head())

    # 4. تحليل سريع: توزيع الشخصيات حسب لون العين
    if 'EYE' in my_data.columns:
        eye_counts = my_data['EYE'].value_counts()
        eye_counts.plot(kind='bar', title='توزيع الشخصيات حسب لون العين')
        plt.xlabel('لون العين')
        plt.ylabel('عدد الشخصيات')
        plt.show()

except FileNotFoundError:
    print("خطأ: لم يتم العثور على الملف. تأكد من إرفاق Dataset الصحيحة في Kaggle.")
except Exception as e:
    print(f"حدث خطأ غير متوقع: {e}")
