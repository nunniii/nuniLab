# that's nunito's laboratory 🧪🛰️

(portuguese)
## Álgebra booleana

**[➡️./c/](./c/) é uma representação básica de como os operadores lógicos agem no nível da ULA.**

```rust
// (false, true) = (0, 1)

// AND
fn and(n1:u8, n2:u8) -> u8 {
    return n1 * n2; // Retorna 0b0 se qualquer dos argumentos for 0b0.
}

// OR
fn or(n1:u8, n2:u8) -> u8 {
    return n1 + n2; // Retorna 0b1 se qualquer dos argumentos for 0b1.
}

// NOT
fn not(n:u8) -> u8 {
    return 1 - n; // Retorna 0b0 caso o argumento seja 0b1, e portanto, retorna 0b1 caso o argumento seja 0b0.
}


```
Estas funções fornecem retorno binário [0 | 1]. Para que os valores não extrapolassem [a, b] != [0, 1], adicionei algumas medidas de programação.

**A álgebra booleana:**

![image](https://github.com/nunniii/nuniLab/assets/69170710/f168d19c-ce18-4dd4-acbd-3c90ad669a3c)


Trabalar com álgebra no nivel binário, é importante pois podemos fazer otimizações de processamentos da ULA através de vários conceitos matemáticos, como os teoremas De Morganum que constitui um dos principais: 

![image](https://github.com/nunniii/nuniLab/assets/69170710/21c5e4e2-83e1-4851-aa83-b3e9c9dcff81)




