import fitz
import sys

doc = fitz.open('مسار_ملف_البي_دي_اف')

for page in doc:

    text = page.get_text('text')

    with open(f'اسم_الملف_الناتح', 'a', encoding='utf-8') as f:

        sys.stdout = f

        print(text)
