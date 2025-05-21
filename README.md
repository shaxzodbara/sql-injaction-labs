# SQL Injection Lab - Flask ilovasi

Bu loyiha SQL Injection zaifligini o‘rganish va sinovdan o‘tkazish uchun mo‘ljallangan Flask ilovasidir. Unda foydalanuvchilar login qilishi mumkin va noto‘g‘ri yozilgan SQL so‘rovi orqali admin panelga kirish imkoniyati mavjud.

## Xususiyatlar

- SQL Injection zaifligi mavjud (`login` sahifasida)
- Foydalanuvchi agenti, IP manzili va login urinishlari loglanadi
- Admin panel orqali barcha login urinishlarini ko‘rish mumkin (`/logs`)
- Lokal tarmoqdagi boshqa qurilmalar ham kirishi mumkin

## run

1. Loyihani klonlash yoki `.zip` holatda yuklab oling.
2. Terminalda quyidagilarni bajaring:


pip install -r requirements.txt
python app.py
