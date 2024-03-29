# Mavzu 20: Exception - istisno

<!-- TOC -->
* [Xatolar - dasturchining kundalik noni](#xatolar---dasturchining-kundalik-noni)
* [Noto'g'ri ma'lumotlar kiritilgandagi xatolik](#notog--ri-malumotlar-kiritilgandagi-xatolik)
* [try-except bloklari](#try-except-bloklari)
* [Bir nechta istisno bilan ishlash](#bir-nechta-istisno-bilan-ishlash)
* [Standart istisno va undan foydalanish](#standart-istisno-va-undan-foydalanish)
* [Ba'zi foydali istisnolar](#bazi-foydali-istisnolar)
<!-- TOC -->

# Xatolar - dasturchining kundalik noni

Barcha dasturchilar (jumladan, siz) xatosiz kod yozishni xohlashlari va bu maqsadga erishish uchun qo'llaridan kelganini qilishlari shubhasiz ko'rinadi. Afsuski, bu dunyoda hech narsa mukammal emas va dasturiy ta'minot bundan mustasno emas.

Xato qilish insonga xosdir. Hech qanday xatoga ega bo'lmagan kod yozish mumkin emas. Bizni noto'g'ri tushunmang - biz sizni noto'g'ri va xatoga boy dasturlar yozish fazilat demoqchimasmiz. Biz eng ehtiyotkor dasturchi ham kichik yoki katta xatoyu kamchiliklardan qochib qutula olmasligini tushuntirmoqchimiz. Faqat hech narsa qilmaydiganlar xato qilmaydi.


Ajablanarlisi shundaki, bu qiyin haqiqatni qabul qilish sizni yaxshi dasturchiga aylantirishi va kod sifatini yaxshilashi mumkin.

"Bu qanday bo'lishi mumkin?", deb so'rashingiz mumkin.

Keyingi mavzularda sizga tushuntirishga harakat qilamiz.
 

**Ma'lumotlardagi xatolar va koddagi xatolar**

Dasturlashdagi xatolar kamida ikki turli bo'ladi. Birinchisi  sizning kodingiz noto'g'ri ma'lumotlar bilan ta'minlanganda istisno yuzaga keladi. Misol uchun, dasturga butun sonni kiritish kerak, ammo ehtiyotsiz foydalanuvchi uning o'rniga tasodifiy harflarni kiritadi.

Shunda sizning kodingizda istisno yuz berib, to'xtab qoladi va foydalanuvchi ekraniga qisqa va noaniq xato xabari chiqishi mumkin. Foydalanuvchi vaziyatdan qoniqmaydi va siz ham qoniqmasligingiz kerak.

Biz sizga kodingizni bunday nosozlikdan qanday himoya qilishni va foydalanuvchining g'azabini qo'zg'atmaslikni ko'rsatamiz.

Ikkinchisi siz dasturni yozishda xatolarga yo'l qo'yganingiz tufayli namoyon bo'ladi. Bunday xatolik odatda "bug" (tarjimasi suvarak) deb ataladi, bu dastur yomon ishlayotgan bo'lsa, u kompyuter uskunasi ichida yashaydigan va qisqa tutashuvlar yoki boshqa shovqinlarni keltirib chiqaradigan zararli suvaraklar sabab bo'lishi kerak, degan mustahkam ishonchning namoyonidir.

Avallari kompyuterlar katta zallarni egallagan, kilovatt elektr energiyasini iste'mol qilgan va juda katta issiqlik ishlab chiqaradigan paytlarda bunday hodisalar tez-tez sodir bo'lgan. Yaxshiyamki yoki yo'q, bu vaqtlar o'tib ketdi va kodingizni buzishi mumkin bo'lgan yagona xatolar koddagi xatolardir. Shuning uchun, biz sizga xatolaringizni qanday topish va yo'q qilishni, boshqacha qilib aytganda, kodingizni qanday tuzatishni ko'rsatishga harakat qilamiz.

Keling, xatolar va xatolar mamlakati bo'ylab sayohatni boshlaylik.

# Noto'g'ri ma'lumotlar kiritilgandagi xatolik

Keling, juda sodda kodning bir qismini yozamiz - u natural sonni (manfiy bo'lmagan butun son) o'qiydi va 1/qiymat formulasi natijasini chop etadi. Shu tarzda, `2` raqamidan `0.5` (1/2) va `4` raqamidan `0.25` (1/4) hosil bo'ladi. Mana dastur:

```python
raqam = int(input('Natural raqam kiriting: '))
print(f'1/{raqam} = {1/raqam}')
```
Kodda biron xatolik ko'ryapsizmi? Kod shunchalik qisqa va soddaki,  u yerda hech qanday muammo yo'qdek ko'rinadi.

Ha, siz haqsiz - butun son bo'lmagan ma'lumotlarni kiritish (bu hech narsa kiritmaslikni ham o'z ichiga oladi) dasturning to'g'ri bajarilishini butunlay buzadi. Kod foydalanuvchisiga quyidagi ko'radi:

```text
Traceback (most recent call last):
  File "C:\Users\hp\PycharmProjects\Foundation_exercices\main.py", line 1, in <module>
    raqam = int(input('Natural raqam kiriting: '))
ValueError: invalid literal for int() with base 10: ''
```
Xatolik haqidagi habarning oxirgi qatoriga ahamiyat bering. Qatordagi birinchi so'z kodingiz to'xtab qolishiga olib keladigan xatolik/istisno nomidir. Bu ValueError. Qatorning qolgan qismi faqat qisqacha tushuntirish bo'lib, u yuzaga kelgan istisno sababini aniqroq tushuntiradi.

Bu xatolikni qanday qilib oldini olish mumkin.

Sizning hayolingizga kelishi mumkin bo'lgan birinchi fikr, foydalanuvchi tomonidan taqdim etilgan ma'lumotning (`raqam`) haqiqiyligini tekshirish va agar ma'lumotlar noto'g'ri bo'lsa, formulani hisoblamaslik. Bunday holda, foydalanuvchi kiritgan qiymatni son ekanligini tekshirishimiz kerak bo'ladi

`raqam` oʻzgaruvchining turi int ekanligini tekshirish uchun biz type operatoridan foydalanamiz:

```python
type(raqam) is int
```
Agar `raqam` int bo'lsa, uning natijasi True bo'ladi


# try-except bloklari

```text
try:
	# Bu yerda xatolik yuzaga kelishi mumkin bo'lga kod yoziladi
except:
	# Xatolik yuz berganda nima chora ko'rish kerak bo'lsa, usha shu yerga yoziladi

```

Bu yerda ikkita blokni ko'rishingiz mumkin:

- birinchisi, `try` kalit so'zidan boshlab - bu siz xavfli deb gumon qilgan kodni qo'yadigan joy; Eslatma: bunday xatolik istisno deb ataladi,
- ikkinchisi, kodning `except` kalit so'zi bilan boshlanadigan qismi istisnoni boshqarish uchun mo'ljallangan; Bu yerda nima qilishni xohlayotganingiz sizga bog'liq: siz tartibsizlikni hal qilishingiz yoki muammoga ko'z yumishingiz mumkin (garchi biz birinchi yechimni afzal ko'rsak ham).

Shunday qilib, bu ikki blok shunday ishlaydi, deb aytishimiz mumkin:

try kalit so'zi ruxsatsiz biror narsa qilishga harakat qiladigan joyni belgilaydi;
istisno kalit so'zi uzr so'rash qobiliyatingizni namoyish qilishingiz mumkin bo'lgan joyni boshlaydi.
Ko'rib turganingizdek, bu yondashuv xatolarni umuman oldini olish o'rniga xatolarni qabul qiladi.

Keling, kodga Python yondashuvini tadbiq qilish uchun kodni qayta yozamiz:

```python
try:
    raqam = int(input('Natural raqam kiriting: '))
    print(f'1/{raqam} = {1/raqam}')       
except:
    print('Raqam kiritish kerak edi.')

```

Keling, nima haqida gaplashganimizni umumlashtiramiz:

- `try` va `except` o'rtasida joylashgan kodning har qanday qismi juda o'ziga xos tarzda bajariladi - bu yerda yuzaga keladigan har qanday **xato dasturning bajarilishini to'xtatmaydi**. Buning o'rniga boshqaruv darhol `except` kalit so'zidan keyin joylashgan birinchi qatorga o'tadi va `try` bo'limining qolgan qismi bajarilmaydi;
- `except` bo'limidagi kod faqat `try` blokida istisnoga duch kelganida faollashadi. Boshqa yo'l bilan u yerga borishning iloji yo'q;
- `try` bloki yoki `except` bloki muvaffaqiyatli bajarilganda, boshqaruv oddiy bajarilish yo'liga qaytadi va boshqa kodlar hech narsa bo'lmagandek bajariladi.

Endi biz sizga savol bermoqchimiz: `ValueError` boshqaruvning `except` blokiga tushishi mumkin bo'lgan yagona yo'lmi?

Kodni diqqat bilan tahlil qiling va javobingizni o'ylab ko'ring!

# Bir nechta istisno bilan ishlash

Istisno qilishning bir nechta mumkin bo'lgan usullari mavjud. Misol uchun, foydalanuvchi kirish sifatida nol kiritishi mumkin - keyin nima bo'lishini taxmin qila olasizmi?

Ha, siz haqsiz - `print()` funksiyasi chaqiruviga joylashtirilgan bo'linish `ZeroDivisionError` istisnosini chaqiradi. Siz kutganingizdek, kodning harakati avvalgi holatda bo'lgani kabi bo'ladi - foydalanuvchi "Raqam kiritish kerak edi." xabarini ko'radi, aslida '0 raqamini kiritish mumkin emas' degan habarni berish tushunarliroq bo'lar edi, . Shuning uchun bunday muammoni biroz boshqacha hal qilish kerak.

Bu yerda kamida ikkita yondashuv mavjud.

Ulardan birinchisi bir vaqtning o'zida oddiy va murakkab: ikkita alohida `try` blokini qo'shishingiz mumkin, ulardan biri `ValueError` paydo bo'lishi mumkin bo'lgan `input()` funktsiyasini chaqirish, ikkinchisi esa bo'linish natijasida yuzaga kelishi mumkin bo'lgan muammolarni hal qilishga qaratilgan. Bu ikkala `try` bloklarlarining har birida o'zlarining `except` bloklariga ega bo'ladi va aslida siz ikki xil xato ustidan to'liq nazoratni qo'lga kiritasiz.

Bu yechim yaxshi, lekin u biroz uzun - keraksiz kodlar ko'payib ketadi. Bundan tashqari, bu sizni kutayotgan yagona xavf emas. E'tibor bering, birinchi `try-except` blokini tark etish juda ko'p noaniqliklarni qoldiradi - foydalanuvchi kiritgan qiymat bo'linishda foydalanish uchun xavfsiz bo'lishini ta'minlash uchun siz qo'shimcha kod qo'shishingiz kerak bo'ladi. Shunday qilib, oddiy tuyulgan yechim haddan tashqari murakkablashadi.

Yaxshiyamki, Python bunday qiyinchiliklarni engishning oddiy usulini taklif qiladi.

**Bitta try va ikkita istisno**

Quyidagi kodga qarang. Ko'rib turganingizdek, biz ikkinchi `except` blokini joriy qildik. Bu yagona farq emas - ikkala blokda ham **except nomlari** ko'rsatilganligini unutmang. Ushbu variantda kutilgan istisnolarning har biri xatoni hal qilishning o'ziga xos usuliga ega, ammo shuni ta'kidlash kerakki, barcha bloklardan **faqat bittasi boshqaruvni to'xtata oladi** - _agar bloklardan biri bajarilsa, qolgan barcha bloklar bajarilmay qoladi_.

```python
try:
    raqam = int(input('Natural raqam kiriting: '))
    print(f'1/{raqam} = {1/raqam}')       
except ValueError:
    print('Raqam kiritish kerak edi.')   
except ZeroDivisionError:
    print("0 raqamiga bo'lish mumkin emas")
```


Bundan tashqari, `except` bo'limlar soni cheklanmagan - siz ulardan kerakli darajada ko'p yoki bir nechtasini belgilashingiz mumkin, lekin istisnolardan **hech biri bir martadan ortiq belgilanishi mumkin emasligini unutmang.**

# Standart istisno va undan foydalanish

Kod yana o'zgardi - farqni ko'ra olasizmi?

```python
try:
    raqam = int(input('Natural raqam kiriting: '))
    print(f'1/{raqam} = {1/raqam}')       
except ValueError:
    print('Raqam kiritish kerak edi.')   
except ZeroDivisionError:
    print("0 raqamiga bo'lish mumkin emas")    
except:
    print('Qandaydur muammo yuzaga keldi!')
```
Biz bu gal uchinchi except blokini qo'shdik, lekin bu safar unda istisno nomi ko'rsatilmagan – biz uni anonim yoki (uning haqiqiy roliga yaqinroq) standart deb aytishimiz mumkin. Istisno ko'tarilganda va ushbu istisnoga mos except bloki bo'lmasa, u standart istisno bloki tomonidan boshqarilishini kutishingiz mumkin.

**Eslatma**
Standart istisno bloki eng so'ngi except bloki bo'lishi kerak

# Ba'zi foydali istisnolar

Keling, ba'zi foydali (aniqrog'i, eng ko'p tarqalgan) istisnolarni batafsil ko'rib chiqamiz.

**ZeroDivisionError** - 0ga bo'lish istisnosi

Bu Python biror sonni 0 raqamiga bo'lish operatsiyani bajarayotgan paytda paydo bo'ladi. Shuni esda tutingki, bir nechta Python operatorlari ushbu istisnoni chaqirishi mumkin. Ular qaysilar?

Ular: `/`, `//` va `%`.

**ValueError** - qiymat bo'yicha istisno

Bu istisno funksiyaga kutilmagan qiymatni berganda sodir bo'ladi. 

```python
b = int('son') 
```
Natija:
```text
Traceback (most recent call last):
  File "C:\Users\hp\Documents\main.py", line 1, in <module>
    b = int('son')
ValueError: invalid literal for int() with base 10: 'son'
```

`int()` funksiyasiga sondan iborat `str` ma'lumot turini berish kerak edi, lekin bu yerda **son emas harflar berilgan**

**TypeError** - ma'lumot turi bo'yicha istisno

Ushbu istisno ma'lumot turi joriy kontekstda qabul qilinishi mumkin bo'lmagan ma'lumotlarni qo'llagan paytda sodir bo'ladi. Misolga qarang:

```python
short_list = [1] 
one_value = short_list[0.5]
```

Roʻyxat indeksi sifatida float qiymatidan foydalanishga ruxsat berilmagan (xuddi shu qoida kortejlar uchun ham amal qiladi). 

**AttributeError** - hususiyat/metod xatosi

Ushbu istisno elementda mavjud bo'lmagan hususiyat/metodni ishlatmoqchi bo'lganda sodir bo'ladi. Masalan:


```python
short_list = [1] 
short_list.append(2) 
short_list.depend(3)
```
Bizning misolimizning uchinchi qatori ro'yxatlarda mavjud bo'lmagan metod yozilgan. Bu `AttributeError` istisnosini chaqiradi.

**SyntaxError** - sintaksis bo'yicha istisno

Ushbu istisno, Python grammatikasini buzilishiga olib keladigan kod yozganda sodir bo'ladi. Bunday turdagi ba'zi xatolarni kodni ishga tushirmasdan aniqlab bo'lmaydi. Bunday xatti-harakatlar interpretator tillarga xosdir, ya'ni interpretator butun manba kodini skanerlamasdan kodni ishga tushiradi, shunda ishlash jarayonida SyntaxError xatoligi sodir bo'ladi. Ba'zida ishga tushmasdan sodir bo'ladi. 

Dasturlaringizda bu istisnoni `try-exept` blokida qayta ishlash yomon fikr. Chunki siz sabab bo'lgan xatolarni maskalash o'rniga, sintaksik xatolardan xoli kod yozishingiz kerak.