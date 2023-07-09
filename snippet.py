import fitz
import sys
from bidi import algorithm

doc = fitz.open('مسار_ملف_البي_دي_اف')

for page in doc:

    text = page.get_text('text')

    with open(f'اسم_الملف_الناتح.txt', 'a', encoding='utf-8') as f:

        sys.stdout = f

        # للفة العربية ابقي على السطر 18
        # أما إذا كان الملف باللغة الانكليزية فامسح السطر 18
        text = algorithm.get_display(text)

        print(text)
