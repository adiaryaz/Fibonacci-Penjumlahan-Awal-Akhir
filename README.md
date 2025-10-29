# Fibonacci & Penjumlahan Awal Akhir

Sebuah program untuk menghasilkan deret Fibonacci kustom menggunakan array dan kemudian menjumlahkan elemen-elemennya dari kedua ujung.

## 📝 Deskripsi

Program ini menyelesaikan masalah dalam dua tahap berdasarkan tiga input integer (`n`, `base1`, `base2`):

1.  **Pembuatan Deret (Baris 1):** Program akan membuat deret angka yang mirip dengan Fibonacci. Deret ini dimulai dengan `base1` dan `base2`. Sebanyak `n` angka baru akan dibuat, di mana setiap angka baru adalah hasil penjumlahan dari dua angka sebelumnya. Total panjang deret dalam array adalah $n + 2$.
2.  **Penjumlahan Awal-Akhir (Baris 2):** Program akan membuat deret baru berdasarkan hasil deret pertama. Deret kedua ini dibentuk dengan menjumlahkan elemen pertama dan elemen terakhir, lalu elemen kedua dan elemen kedua terakhir, dan seterusnya, bergerak menuju ke tengah.
      * Jika jumlah elemen di deret pertama **genap**, semua elemen akan memiliki pasangan.
      * Jika jumlah elemen **ganjil**, elemen yang berada tepat di tengah akan ditampilkan apa adanya setelah semua pasangan lainnya dijumlahkan.

-----

## 🎯 Problem Statement

### Input:

  * Input 1: `n` (Integer, jumlah langkah/elemen baru yang akan dibuat).
  * Input 2: `base1` (Integer, angka pertama deret).
  * Input 3: `base2` (Integer, angka kedua deret).

### Output:

  * **Baris 1:** Deret Fibonacci kustom, dengan elemen dipisahkan oleh spasi.
  * **Baris 2:** Deret hasil penjumlahan "awal-akhir", dengan elemen dipisahkan oleh spasi.
  * **"Undefined"** jika input `n` tidak valid.

### Rules:

1.  Input pertama (`n`) harus merupakan bilangan bulat **positif** ($n \ge 1$).
2.  Jika $n < 1$, program harus menampilkan **"Undefined"**.
3.  Deret pertama (Baris 1) akan selalu memiliki panjang $n + 2$.
4.  Deret kedua (Baris 2) akan memiliki panjang $\lceil (\frac{n + 2}{2}) \rceil$.

-----

## 💡 Examples

### Example 1 (Sample 1)

**Input:**

```
5
2
3
```

**Output:**

```
2 3 5 8 13 21 34
36 24 18 8
```

**Explanation:**

  * **Baris 1:** Dimulai dengan `2 3`. Menghasilkan `n=5` elemen baru (2+3=**5**, 3+5=**8**, 5+8=**13**, 8+13=**21**, 13+21=**34**). Total 7 elemen.
  * **Baris 2:** Dihitung dari `[2, 3, 5, 8, 13, 21, 34]`.
      * `2 + 34 = 36`
      * `3 + 21 = 24`
      * `5 + 13 = 18`
      * `8` (elemen tengah, tidak memiliki pasangan)

### Example 2 (Sample 2)

**Input:**

```
18
-5
3
```

**Output:**

```
-5 3 -2 1 -1 0 -1 -1 -2 -3 -5 -8 -13 -21 -34 -55 -89 -144 -233 -377
-382 -230 -146 -88 -56 -34 -22 -14 -10 -8
```

**Explanation:**

  * **Baris 1:** Dimulai dengan `-5 3`. Menghasilkan `n=18` elemen baru. Total 20 elemen.
  * **Baris 2:** Dihitung dari array 20 elemen (genap).
      * `-5 + (-377) = -382`
      * `3 + (-233) = -230`
      * ... (seterusnya ke tengah)
      * `-3 + (-5) = -8`

### Example 3 (Sample 3)

**Input:**

```
0
3
4
```

**Output:**

```
Undefined
```

**Explanation:** Input `n=0` tidak valid, karena input step tidak boleh kurang dari 1.

### Example 4 (Contoh dari Deskripsi)

**Input:**

```
1
5
2
```

**Output:**

```
5 2 7
12 2
```

**Explanation:**

  * **Baris 1:** Dimulai dengan `5 2`. Menghasilkan `n=1` elemen baru (5+2=**7**). Total 3 elemen.
  * **Baris 2:** Dihitung dari `[5, 2, 7]`.
      * `5 + 7 = 12`
      * `2` (elemen tengah)

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/fibonacci-array-sum.git
    cd fibonacci-array-sum
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Masukkan `n`, `base1`, dan `base2` pada baris terpisah saat diminta untuk melihat hasilnya.
