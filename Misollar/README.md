# 08: Shartli operator (if/elif/else)
 

**Reja:**
<!-- TOC -->
* [08: Shartli operator (if/elif/else)](#08--shartli-operator--ifelifelse-)
    * [Qayatirish uchun](#qayatirish-uchun)
      * [Sonlarni solishtirish](#sonlarni-solishtirish)
      * [Satrlarni solishtirish](#satrlarni-solishtirish)
      * [Sonlarni tekshirish](#sonlarni-tekshirish)
      * [Arifmetik operatorlar](#arifmetik-operatorlar)
      * [And va Or](#and-va-or)
      * [if, elif va else](#if-elif-va-else)
    * [Misollar](#misollar)
        * [if ifodasi uhcun misol](#if-ifodasi-uhcun-misol)
        * [else ifodasi uhcun misol](#else-ifodasi-uhcun-misol)
        * [else if ifodasi uhcun misol](#else-if-ifodasi-uhcun-misol)
        * [if .. elif .. else ifodasi uhcun misol](#if--elif--else-ifodasi-uhcun-misol)
        * [switch case ifodasi uhcun misol](#switch-case-ifodasi-uhcun-misol)
        * [Ternar operator uhcun misol](#ternar-operator-uhcun-misol)
        * [Tarmoqli if ifodasi uhcun misol](#tarmoqli-if-ifodasi-uhcun-misol)
        * [switch range ifodasi uhcun misol](#switch-range-ifodasi-uhcun-misol)
        * [if va for/while ifodasi uhcun misol](#if-va-forwhile-ifodasi-uhcun-misol)
<!-- TOC -->

### Qayatirish uchun

#### Sonlarni solishtirish

<table>
<tr><td>№</td><td>Nomi</td><td>Misol</td><td>Javobi</td></tr>
<tr><td>1</td><td>3 soni 6 sonidan kattami?</td><td>3 > 6</td><td>False</td></tr>
<tr><td>2</td><td>3 soni 6 sonidan kichikmi?</td><td>3 < 6</td><td>True</td></tr>
<tr><td>3</td><td>3 soni 6 sonidan katta yoki tengmi?</td><td>3 >= 6</td><td>False</td></tr>
<tr><td>4</td><td>3 soni 6 sonidan kichik yoki tengmi?</td><td>3 <= 6</td><td>True</td></tr>
<tr><td>5</td><td>3 soni 6 soniga tengmi?</td><td>6 == 4</td><td>False</td></tr>
<tr><td>6</td><td>3 soni 6 soniga teng emasmi?</td><td>6 != 3</td><td>True</td></tr>
<tr><td>7</td><td>6 soni 0 ga tengmi?</td><td>not 6</td><td>False</td></tr>
</table>

<br>

#### Satrlarni solishtirish

soz1 = 'dastur'<br>
soz2 = 'dasturchi'<br>
soz3 = ''<br>
<table>
<tr><td>№</td><td>Nomi</td><td>Misol</td><td>Javobi</td><td>Izoh</td></tr>
<tr><td>1</td><td>'a' ning kodi 'b' ning kodidan kattami?</td><td>'a' > 'b'</td><td>false</td><td>ord('a') > ord('b')</td></tr>
<tr><td>2</td><td>'a' ning kodi 'b' ning kodidan kichikmi?</td><td>'a' < 'b'</td><td>true</td><td>ord('a') < ord('b')</td></tr>
<tr><td>3</td><td>soz1 bilan soz2 bir xilmi?</td><td>soz1 == soz2</td><td>false</td><td></td></tr>
<tr><td>4</td><td>soz1 bilan soz2 bir xil emasmi?</td><td>soz1 != soz2</td><td>true</td><td></td></tr>
<tr><td>5</td><td>soz1 bo'sh satrmi?</td><td> not soz1</td><td>false</td><td></td></tr>
<tr><td>6</td><td>soz3 bo'sh satrmi?</td><td>not soz3</td><td>true</td><td></td></tr>
 <tr><td>6</td><td>soz2 ichida soz1 uchraydimi?</td><td>soz1 in soz2</td><td>true</td><td></td></tr>
</table>

<br>


#### Sonlarni tekshirish

son = 10 <br>

<br>
<table>
<tr><td>№</td><td>Nomi</td><td>Misol</td><td>Javobi</td></tr>
<tr><td>1</td><td>son musbatmi?</td><td>son > 0</td><td>True</td></tr>
<tr><td>2</td><td>son manfiymi?</td><td>son < 0</td><td>False</td></tr>
<tr><td>3</td><td>son juftmi?</td><td>son % 2 == 0</td><td>True</td></tr>
<tr><td>4</td><td>son toqmi?</td><td>son % 2 == 1</td><td>False</td></tr>
<tr><td>5</td><td>son 5 ga karralikmi?</td><td>son % 5 == 0</td><td>True</td></tr>
<tr><td>6</td><td>son 5 ga karralik emasmi?</td><td>son % 5 != 0</td><td>False</td></tr>
</table>

<br>

#### Arifmetik operatorlar

Arifmetik operatorlar oddiy matematik amallarni bajarish uchun ishlatiladi:
<table>
<tr><td>Operator</td><td>Nomi</td><td>Misol</td><td>Javobi</td></tr>
<tr><td>+</td><td>Qo'shish</td><td>3 + 6</td><td>9</td></tr>
<tr><td>-</td><td>Ayirish</td><td>3 - 6</td><td>-3</td></tr>
<tr><td>*</td><td>Ko'paytirish</td><td>3 * 6</td><td>18</td></tr>
<tr><td>/</td><td>Bo'lish</td><td>6 / 3</td><td>2.0</td></tr>
<tr><td>%</td><td>Qoldiq olish</td><td>7 % 4</td><td>3</td></tr>
</table>

<br>


#### And va Or

| Operator | Ma'nosi                                                                                                                                                                            | Misol           | Natija |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|--------|
| And      | Bir paytda bajarilishi kerakligini bildiradi. <br/>Agar ikkala shart True bo'lsagina, natija True bo'ladi va <br/>if bloki ishga tushadi, aks holda else bloki yoki elif blokiga o'tadi | a > 0 and b > 0 | True   |
| Or       | Kamida bitta shart bajarilishi kerakligini bildiradi. <br/>Ikkala shartlardan kamida bittasi bajarilsa, <br/>if bloki aks holda, else bloki ishga tushadi                               | a < 0 or b < 0  | False  |

#### if, elif va else


<table>
<tr><td>Operator</td><td>Misol</td></tr>
<tr><td>if</td><td>

```c
#include <stdio.h>

int main() {
    int son = 10;

    if (son > 10) {
        son = son + 2;
    }

    return 0;
}

```

</td></tr>
<tr><td>else</td><td>

```c
#include <stdio.h>

int main() {
    int a = 100;
    int b = 100;

    if (a > b) {
        printf("a soni b sonidan katta\n");
    } else if (a == b) {
        printf("a soni b soniga teng\n");
    }

    return 0;
}

```

</td></tr>
<tr><td>else if</td><td>

```c
#include <stdio.h>

int main() {
    int kun = 5;

    if (kun >= 1 && kun <= 4) {
        printf("Ish kuni\n");
    } else if (kun >= 5 && kun <= 6) {
        printf("Dam olish kuni\n");
    } else {
        printf("Bunday kun mavjud emas\n");
    }

    return 0;
}

```

</td></tr>
<tr><td>ichma-ich if</td><td>

```c
#include <stdio.h>

int main() {
    int son;

    // Foydalanuvchidan sonni kiritishni so'rash
    printf("Son kiriting: ");
    scanf("%d", &son);

    // Sonni tekshirish
    if (son > 0) {
        if (son > 50) {
            printf("50 dan katta\n");
        } else {
            printf("50 dan kichik\n");
        }
    } else {
        printf("Musbat son kiriting\n");
    }

    return 0;
}

```

</td></tr>

</table>

<br>

### Misollar
##### if ifodasi uhcun misol 

1. a = 300 va b = 200. Agar a soni b sonidan katta bo'lsa, ekranga "a soni b sonidan katta" yozuvi chiqsin

Kod:

```c
#include <stdio.h>

int main() {
    int a = 300;
    int b = 200;

    if (a > b) {
        printf("a soni b sonidan katta\n");
    }

    return 0;
}
```

Natija:

```text
a soni b sonidan katta
```

##### else ifodasi uhcun misol

2. a = 100 va b = 200. Agar a soni b sonidan katta bo'lsa, ekranga "a soni b sonidan katta" yozuvi chiqsin. Aks holda agar "a soni b sonidan katta emas" yozuvi chiqsin

Kod:

```c
#include <stdio.h>

int main() {
    int a = 100;
    int b = 100;

    if (a > b) {
        printf("a soni b sonidan katta\n");
    } else {
        printf("a soni b sonidan katta emas\n");
    }

    return 0;
}

```

Natija:

```text
a soni b sonidan kichik
```


##### else if ifodasi uhcun misol

3. a = 100 va b = 100. Agar a soni b sonidan katta bo'lsa, ekranga "a soni b sonidan katta" yozuvi chiqsin. Agar a soni b soniga teng bo'lsa "a soni b soniga teng" yozuvi chiqsin

Kod:

```c
#include <stdio.h>

int main() {
    int a = 100;
    int b = 100;

    if (a > b) {
        printf("a soni b sonidan katta\n");
    } else if (a == b) {
        printf("a soni b soniga teng\n");
    }

    return 0;
}

```
Natija:

```text
a soni b soniga teng
```

##### if .. elif .. else ifodasi uhcun misol

4. Svetofor dasturini yasaymiz. Bizda svetofor o'zgaruvchisi bor. Uning qiymatlari *qizil*, *yashil* va *sariq* bo'lishi mumkin. Agar yashil bo'lsa, ekranga 'Yuring!' yozuvi chiqsin, aks holda agar *sariq* bo'lsa, 'Tayyorlaning!' habari chiqsin, aks holda 'To'xtang!' yozuvi chiqsin

Kod:

```c
#include <stdio.h>
#include <string.h>

int main() {
    char svetofor[10];

    // Foydalanuvchidan qiymat olamiz
    printf("Svetofor rangini kiriting (yashil, sariq, qizil): ");
    scanf("%s", svetofor);

    // natijani solishtirib ekranga chiqarish
    if (strcmp(svetofor, "yashil") == 0) {
        printf("Yuring!\n");
    } else if (strcmp(svetofor, "sariq") == 0) {
        printf("Tayyorlaning!\n");
    } else {
        printf("To'xtang! Qizil yondi yoki svetofor ishlamayapti :)\n");
    }

    return 0;
}

```

Natija:

```text
Svetofor rangini kiriting (yashil, sariq, qizil): sariq
Tayyorlaning!
```

```text
Svetofor rangini kiriting (yashil, sariq, qizil): yashil
Yuring!
```

```text
Svetofor rangini kiriting (yashil, sariq, qizil): abc
To'xtang!
```

5. Foydalanuvchidan 10 dan 20 gacha (10 va 20 ham kiradi) raqam kiritishni so'rang. Agar ular ushbu diapazondagi raqamni kiritsa, "Rahmat" xabarini ko'rsating, aks holda "Noto'g'ri javob" xabarini ko'rsating.

Kod:

```c
#include <stdio.h>

int main() {
    int raqam;

    // Foydalanuvchidan raqam kiritishni so'rash
    printf("10 dan 20 gacha (10 va 20 ham kiradi) raqamni kiriting: ");
    scanf("%d", &raqam);

    // Raqamni tekshirish
    if (raqam >= 10 && raqam <= 20) {
        printf("Rahmat\n");
    } else {
        printf("Noto'g'ri javob\n");
    }

    return 0;
}

```

Natija:

```text
10 dan 20 gacha (10 va 20 ham kiradi) raqamni kiriting: 20
Rahmat
```

```text
10 dan 20 gacha (10 va 20 ham kiradi) raqamni kiriting: 40
Noto'g'ri javob
```

##### switch case ifodasi uhcun misol

6. Hafta kunlari raqamiga qarab, kun nomlarini chiqaring

Kod:

```c
#include <stdio.h>

int main() {
    int kun;

    // Foydalanuvchidan qiymatni olish
    printf("Hafta kunini raqam bilan kiriting: ");
    scanf("%d", &kun);

    // hafta kunini aniqlash
    switch (kun) {
        case 1:
            printf("Dushanba\n");
            break;
        case 2:
            printf("Seshanba\n");
            break;
        case 3:
            printf("Chorshanba\n");
            break;
        case 4:
            printf("Payshanba\n");
            break;
        case 5:
            printf("Juma\n");
            break;
        case 6:
            printf("Shanba\n");
            break;
        case 7:
            printf("Yakshan

```

Natija:

```text
Hafta kunini raqam bilan kiriting: 5
Juma
```

```text
Hafta kunini raqam bilan kiriting: 12
Bunday kun mavjud emas
```

##### Ternar operator uhcun misol

7. Agar son juft bo'lsa, "Son muft", toq bo'lsa "Son toq" habari chiqsin. Masalani ternar operatori yordamida bajaring

Kod:

```c
#include <stdio.h>

int main() {
    int a = 100;
    char *habar;

    // Ternar operator yordamida habarni aniqlash
    habar = (a % 2 == 0) ? "Son juft" : "Son toq";

    // Habarni ekranga chiqarish
    printf("%s\n", habar);

    return 0;
}

```

Natija:

```text
musbat
```

##### Tarmoqli if ifodasi uhcun misol

8. Faraz qiling, futbol to'garagiga qatnashish uchun bola 12 ga to'lgan bo'lishi kerak. Agar bola 12 ga to'lgan bo'lsagina, undan kelish soatini so'rang. Ish vaqti 9-18, kelish vaqti ish vaqtiga to'g'ri kelsa, "Rahmat, salomat bo'ling" habari aks holda, "Kechirasiz, bu vaqtda ishlamaymiz" habarini chiqaring. Agarbola 12 ga to'lmagan bo'lsa, u holda "Kechirasiz siz hali juda yosh ekansiz" habarini chiqarsin 

Kod:

```c
#include <stdio.h>

int main() {
    int yosh;
    int kelish_soati;

    // Bola yoshini kiritish
    printf("Bolaning yoshini kiriting: ");
    scanf("%d", &yosh);

    if (yosh >= 12) {
        // Agar bola 12 ga to'lgan bo'lsa, kelish soatini so'rash
        printf("Kelish vaqtingizni (24 soat formatida) kiriting: ");
        scanf("%d", &kelish_soati);

        // Kelish vaqtini tekshirish
        if (kelish_soati >= 9 && kelish_soati <= 18) {
            printf("Rahmat, salomat bo'ling\n");
        } else {
            printf("Kechirasiz, bu vaqtda ishlamaymiz\n");
        }
    } else {
        // Agar bola 12 ga to'lmagan bo'lsa
        printf("Kechirasiz siz hali juda yosh ekansiz\n");
    }

    return 0;
}

```

Natija:

```text
Bolaning yoshini kiriting: 7
Kechirasiz siz hali juda yosh ekansiz
```
```text
Bolaning yoshini kiriting: 14
Kelish vaqtingizni (24 soat formatida) kiriting: 21
Kechirasiz, bu vaqtda ishlamaymiz
```
```text
Bolaning yoshini kiriting: 14
Kelish vaqtingizni (24 soat formatida) kiriting: 10
Rahmat, salomat bo'ling
```


##### switch range ifodasi uhcun misol

9. Foydalanuvchidan haroratni Selsiy bo'yicha kiritishni so'rang. Dastur quyidagi haroratga asoslangan holda tegishli xabarni chop etishi kerak:
Agar harorat -273.15 dan past bo'lsa, harorat noto'g'ri deb chop eting, chunki u 
mutlaq noldan past.
- Agar u aniq -273,15 bo'lsa, harorat mutlaq 0 ekanligini chop eting.
- Agar harorat -273,15 va 0 orasida bo'lsa, harorat muzlash darajasidan past ekanligini chop eting.
- Agar u 0 bo'lsa, harorat muzlash nuqtasida ekanligini chop eting.
- Agar u 0 dan 100 gacha bo'lsa, harorat normal diapazonda ekanligini chop eting.
- Agar u 100 bo'lsa, harorat qaynash nuqtasida ekanligini chop eting.
- Agar u 100 dan yuqori bo'lsa, harorat qaynash nuqtasidan yuqori ekanligini chop eting.

Kod:

```c
#include <stdio.h>

int main() {
    float harorat;

    // Foydalanuvchidan haroratni kiritishni so'rash
    printf("Haroratni Selsiy bo'yicha kiriting: ");
    scanf("%f", &harorat);

    // Harorat diapazonlarini tekshirish
    switch ((int)harorat) {
        // range -273.15 dan past
        case -273 ... -1:  // Noto'g'ri diapazon
            printf("Harorat noto'g'ri: mutlaq noldan past\n");
            break;
        // range -273.15
        case -273:
            printf("Harorat mutlaq 0\n");
            break;
        // range -273.15 dan 0 gacha
        case -1 ... 0:
            printf("Harorat muzlash darajasidan past\n");
            break;
        // range 0
        case 0:
            printf("Harorat muzlash nuqtasida\n");
            break;
        // range 0 dan 100 gacha
        case 1 ... 99:
            printf("Harorat normal diapazonda\n");
            break;
        // range 100
        case 100:
            printf("Harorat qaynash nuqtasida\n");
            break;
        // range 100 dan yuqori
        case 101 ... 999:
            printf("Harorat qaynash nuqtasidan yuqori\n");
            break;
        default:
            printf("Noma'lum holat\n");
            break;
    }

    return 0;
}

```

Natija:

```text
Haroratni Selsiy bo'yicha kiriting: 100
Harorat qaynash nuqtasida
```

```text
Haroratni Selsiy bo'yicha kiriting: 200
Harorat qaynash nuqtasidan yuqori
```

##### if va for/while ifodasi uhcun misol

10. Foydalanuvchidan parol va loginni kiritishni so'raydigan dastur yozing. Agar foydalanuvchi to'g'ri parol va login kiritsa, dastur ularga tizimga kirganligini aytishi kerak. Aks holda, dastur foydalanuvchidan parol va loginni qayta kiritishni so'rashi kerak. Foydalanuvchida beshta urinish bor, beshtadan keyin tizim unga "Sizda urinishlar qolmadi" habari chiqsin

Kod:
```Kod
#include <stdio.h>
#include <string.h>

int main() {
    char kiritilgan_login[100];
    char kiritilgan_parol[100];
    char togri_login[] = "admin"; // To'g'ri login
    char togri_parol[] = "password"; // To'g'ri parol
    int urinish = 0;
    int MAX_ATTEMPTS = 5; // Maksimal urinishlar soni

    while (urinish < MAX_ATTEMPTS) {
        // Foydalanuvchidan login va parolni kiritishni so'rash
        printf("Loginni kiriting: ");
        scanf("%s", kiritilgan_login);
        printf("Parolni kiriting: ");
        scanf("%s", kiritilgan_parol);

        // Login va parolni tekshirish
        if (strcmp(kiritilgan_login, togri_login) == 0 && strcmp(kiritilgan_parol, togri_parol) == 0) {
            printf("Tizimga kirganingiz uchun rahmat!\n");
            return 0; // Dasturdan chiqish
        } else {
            printf("Noto'g'ri login yoki parol. Qayta urinib ko'ring.\n");
            urinish++;
        }
    }

    printf("Sizda urinishlar qolmadi.\n");
    return 0;
}
```

Natija:

```text
Loginni kiriting: admin
Parolni kiriting: sf
Noto'g'ri login yoki parol. Qayta urinib ko'ring.
Loginni kiriting: admin
Parolni kiriting: password
Tizimga kirganingiz uchun rahmat!
```

```text
Loginni kiriting: qw
Parolni kiriting: sd
Noto'g'ri login yoki parol. Qayta urinib ko'ring.
Loginni kiriting: df
Parolni kiriting: er
Noto'g'ri login yoki parol. Qayta urinib ko'ring.
Loginni kiriting: re
Parolni kiriting: er
Noto'g'ri login yoki parol. Qayta urinib ko'ring.
Loginni kiriting: we
Parolni kiriting: e
Noto'g'ri login yoki parol. Qayta urinib ko'ring.
Loginni kiriting: e
Parolni kiriting: df
Noto'g'ri login yoki parol. Qayta urinib ko'ring.
Sizda urinishlar qolmadi.
```

