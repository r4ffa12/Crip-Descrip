# Script de Criptografia e Descriptografia Personalizada

Este repositório contém um script Python que implementa um mecanismo de criptografia e descriptografia personalizado. Ele combina transformações binárias e codificação Base64 para criptografar e descriptografar mensagens de texto usando um vetor binário fixo.

---

## Recursos

- **Conversão Binária**: Converte strings para binário e vice-versa.
- **Operações Bit a Bit**: Inclui inversão, reversão e operações XOR em strings binárias.
- **Codificação Base64**: Codifica os dados binários resultantes em um formato Base64 para facilitar o manuseio.
- **Vetor Fixo Personalizável**: Permite o uso de um vetor binário fixo para operações XOR.

---

## Como Funciona

### Processo de Criptografia
1. **String para Binário**: Converte a string de entrada em uma string binária.
2. **Inversão Binária**: Inverte todos os bits (1 vira 0, e vice-versa).
3. **Reversão Binária**: Reverte a string binária.
4. **Operação XOR**: Aplica uma operação XOR com um vetor binário fixo.
5. **Binário para Base64**: Codifica a string binária resultante em um formato Base64.

### Processo de Descriptografia
1. **Base64 para Binário**: Decodifica a string Base64 de volta para uma string binária.
2. **Operação XOR Reversa**: Aplica uma operação XOR com o mesmo vetor binário fixo.
3. **Reversão Binária**: Reverte a string binária.
4. **Inversão Binária**: Reverte os bits para o estado original.
5. **Binário para String**: Converte a string binária de volta para um texto legível.

---

## Uso

### Criptografia
A função `encrypt` recebe dois parâmetros:
- `input_string`: A string a ser criptografada.
- `fixed_vector`: Uma string binária usada para a operação XOR (deve ser pelo menos do mesmo tamanho que a representação binária da entrada).

Exemplo:
```python
input_string = "Hello, World!"
fixed_vector = "10101010101010101010101010101010" * 10

encrypted = encrypt(input_string, fixed_vector)
print("Base64 Criptografado:", encrypted)
```

### Descriptografia
A função `decrypt` recebe dois parâmetros:
- `encrypted_base64`: A string Base64 a ser descriptografada.
- `fixed_vector`: O mesmo vetor binário usado durante a criptografia.

Exemplo:
```python
encrypted_base64 = "o3Mj++dR0mOn"
fixed_vector = "10101010101010101010101010101010" * 10

decrypted = decrypt(encrypted_base64, fixed_vector)
print("Mensagem Descriptografada:", decrypted)
```

---

## Exemplo

### Criptografia
Entrada:
```
Hello, World!
```
Saída:
```
o3Mj++dR0mOn
```

### Descriptografia
Entrada:
```
o3Mj++dR0mOn
```
Saída:
```
Hello, World!
```

---

## Observações
- O vetor fixo deve permanecer consistente entre a criptografia e a descriptografia.
- Este método de criptografia não é seguro para uso em produção, pois não é resistente a ataques criptográficos.

---

## Licença
Este projeto está licenciado sob a Licença MIT. Fique à vontade para usá-lo e modificá-lo conforme necessário.

---

## Contribuições
Pull requests são bem-vindos. Para mudanças maiores, abra uma issue primeiro para discutir o que você gostaria de alterar.


