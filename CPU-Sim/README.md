```markdown
# 🖥️ Mano Basic Computer — CPU Sim Practicals

A collection of **Computer System Architecture practicals** implemented and tested using **CPU Sim**, based on the **Mano Basic Computer** architecture.

This project covers CPU organization, registers, memory, instruction formats, instruction execution, microoperations, arithmetic and logical operations, program control, input/output, and bit manipulation.

---

## 📚 Concepts Covered

### 🏗️ Basic Computer Organization

- CPU organization
- Registers and memory
- 12-bit addressing
- 16-bit data words
- Instruction formats
- Opcodes and address fields
- Fetch–Decode–Execute cycle
- Microoperations
- Register transfers
- Memory-reference instructions
- Register-reference instructions
- Input/Output instructions
- Arithmetic operations
- Two's complement
- Signed and unsigned representation
- Logical operations
- Conditional skip instructions
- Branching and loops
- Counters and accumulation
- Circular rotation
- Bit manipulation
- AC and E interaction
- CPU simulation and debugging

# 🖥️ A basic computer consists of:

- **CPU** — executes instructions and controls operations
- **Memory** — stores instructions and data
- **ALU** — performs arithmetic and logical operations
- **Control Unit** — generates control signals
- **Registers** — provide fast temporary storage
- **Input/Output** — communicates with external devices

Basic execution flow:

`Fetch → Decode → Execute → Next Instruction`

---

## 🧠 CPU Registers

| Register | Size | Function |
|---|---:|---|
| **AR** | 12-bit | Holds memory address |
| **PC** | 12-bit | Holds address of next instruction |
| **DR** | 16-bit | Holds data transferred to/from memory |
| **AC** | 16-bit | Accumulator for arithmetic and logic |
| **IR** | 16-bit | Holds current instruction |
| **TR** | 16-bit | Temporary storage |
| **INPR** | 8-bit | Input data |
| **OUTR** | 8-bit | Output data |
| **E** | 1-bit | Extend / carry bit |
| **SC** | 4-bit | Sequence counter for control timing |

### Important Registers

**PC — Program Counter**

Stores the address of the next instruction.

**AR — Address Register**

Stores the memory address currently being accessed.

**DR — Data Register**

Temporarily stores data transferred between memory and CPU.

**AC — Accumulator**

Main register used for arithmetic and logical operations.

**IR — Instruction Register**

Stores the instruction currently being executed.

**E — Extend / Carry**

A 1-bit register used with arithmetic and rotate operations.

---

## 💾 Memory

The Mano Basic Computer uses:

- **12-bit addresses**
- **16-bit memory words**
- **4096 (2¹²) memory locations**

Memory stores both instructions and data.

```text
Address → Memory Location → Instruction / Data
```

---

## 🔢 Instruction Format

A memory-reference instruction is 16 bits:

```text
15       14 13 12       11              0
┌────────┬───────────────┬───────────────┐
│ I bit  │    Opcode     │    Address    │
└────────┴───────────────┴───────────────┘
   1 bit       3 bits         12 bits
```

- **I bit** — selects direct or indirect addressing
- **Opcode** — specifies the operation
- **Address** — specifies the memory location

### Direct Addressing

```text
Instruction Address → Operand
```

### Indirect Addressing

```text
Instruction Address → Memory → Actual Address → Operand
```

---

## 🧩 Instruction Categories

### Memory Reference Instructions

```text
AND   ADD   LDA   STA
BUN   BSA   ISZ
```

### Register Reference Instructions

```text
CLA   CLE   CMA   CME
CIR   CIL   INC
SPA   SNA   SZA   SZE
HLT
```

### Input / Output Instructions

```text
INP   OUT
```

---

## 🔄 Fetch Cycle

Every instruction follows the basic cycle:

```text
FETCH → DECODE → EXECUTE → NEXT INSTRUCTION
```

Typical fetch operations include:

```text
PC → AR
M[AR] → IR
PC + 1 → PC
IR(0–11) → AR
decode-IR
```

CPU Sim uses **left-based bit indexing**, so Mano's `IR(0–11)` corresponds to CPU Sim bits `4–15`.

---

### Fetch

The CPU obtains the next instruction from memory.

### Decode

The control unit determines the instruction type, opcode and addressing mode.

### Execute

The CPU performs the operation specified by the instruction.

---

## ⚙️ Microoperations

A machine instruction is executed using smaller register-level operations called **microoperations**.

Examples:

```text
AR ← PC
DR ← M[AR]
IR ← DR
AC ← AC + DR
PC ← PC + 1
```

Relationship:

```text
Machine Instruction
        ↓
Microoperations
        ↓
Control Signals
        ↓
Hardware Operations
```

CPU Sim allows these low-level operations and control sequences to be configured and observed.

---

# ➕ Arithmetic Operations

### Addition

```text
AC ← AC + DR
```

Example:

```text
AC = 10
DR = 5

AC = 15
```

### Subtraction

Subtraction can be performed using two's complement:

```text
A - B = A + Two's Complement(B)
```

### Increment

```text
INC
AC ← AC + 1
```

---

# 🔢 Two's Complement

Two's complement is used to represent signed negative numbers.

Example for `-3`:

```text
 3 = 0000 0000 0000 0011
        ↓ invert
     1111 1111 1111 1100
        ↓ add 1
     1111 1111 1111 1101
```

Therefore:

```text
-3 = FFFD
```

in 16-bit hexadecimal representation.

---

# 🧮 Logical Operations

The practicals cover:

- AND
- OR
- NOT
- XOR
- NAND
- NOR

Basic definitions:

```text
AND  → 1 only when both bits are 1
OR   → 1 when either bit is 1
NOT  → inverts every bit
XOR  → 1 when bits are different
NAND → NOT(AND)
NOR  → NOT(OR)
```

Some operations are constructed using combinations of available Basic Computer instructions rather than being separate machine instructions.

---

# 🔀 Program Control

### BUN — Branch Unconditionally

Transfers execution to a specified address.

```text
PC ← Address
```

### ISZ — Increment and Skip if Zero

Increments a memory value.

If the result becomes zero, the next instruction is skipped.

`ISZ` is therefore useful for implementing counters and loops.

---

# ⏭️ Conditional Skip Instructions

Skip instructions control whether the next instruction executes.

Important instructions:

```text
SPA
SNA
SZA
SZE
```

They test conditions involving:

- AC sign
- AC zero/non-zero
- E zero/non-zero

Conceptually:

```text
Condition?
   ├── True  → Skip next instruction
   └── False → Execute next instruction
```

---

# 🧹 Register Reference Operations

| Instruction | Operation |
|---|---|
| `CLA` | Clear AC |
| `CLE` | Clear E |
| `CMA` | Complement AC |
| `CME` | Complement E |
| `INC` | Increment AC |
| `CIR` | Circular shift right |
| `CIL` | Circular shift left |
| `SPA` | Skip based on AC sign |
| `SNA` | Skip based on AC sign |
| `SZA` | Skip if AC is zero |
| `SZE` | Skip if E is zero |
| `HLT` | Halt execution |

---

# 🔄 Rotate Operations

### CIR — Circular Shift Right

Shifts AC right while involving the **E bit**, allowing circular rotation.

### CIL — Circular Shift Left

Shifts AC left while involving the **E bit**.

These operations demonstrate bit-level manipulation and interaction between AC and E.

---

# 📥 Input / Output

### INP

Transfers input into AC:

```text
Input → INPR → AC
```

### OUT

Transfers AC data to output:

```text
AC → OUTR → Output
```

---

# 🧪 Practicals

## P03 — Addition

Demonstrates:

```text
INP
STA
ADD
OUT
HLT
```

Example:

```text
5 + 7 = 12
```

---

## P04 — Subtraction

Uses two's complement subtraction:

```text
CMA
INC
ADD
```

Example:

```text
18 - 50 = -32
```

---

## P05 — Logic Operations

Demonstrates:

```text
AND
OR
NOT
XOR
NAND
NOR
```

Example:

```text
A = 12
B = 23

AND   = 4
OR    = 31
NOT A = -13
NOT B = -24
XOR   = 27
NOR   = -32
NAND  = -5
```

---

## P06 — Memory Reference

Demonstrates:

```text
LDA
ADD
STA
ISZ
BUN
```

Program repeatedly adds `5` three times.

```text
5 + 5 + 5 = 15
```

---

## P07 — Register Reference

Demonstrates:

```text
CLA
CMA
CME
HLT
```

Final AC after CMA:

```text
FFFF = -1
```

---

## P08 — Conditional Skip

Demonstrates:

```text
INC
SPA
SNA
SZE
```

Covers:

- AC increment
- Sign testing
- Conditional skipping
- E testing

---

## P09 — CIR / CIL

Demonstrates:

```text
CIR
CIL
```

Covers:

- Circular rotation
- Bit manipulation
- AC/E interaction

---

## P10 — Sum Until Negative

Accepts numbers until a negative value is entered.

```text
4
10
0
6
-3
```

Output:

```text
20
```

The negative value terminates the loop and is not included.

---

## P11 — Sum Until Zero

Accepts numbers until zero is entered.

```text
4
10
6
0
```

Output:

```text
20
```

Zero terminates the loop and is not included.

---

# 🔗 Overall Concept Flow

```text
Computer Organization
        ↓
Registers + Memory
        ↓
Instruction Format
        ↓
Fetch / Decode / Execute
        ↓
Microoperations
        ↓
Arithmetic + Logic
        ↓
Memory Reference Instructions
        ↓
Register Reference Instructions
        ↓
Program Control + Loops
        ↓
Input / Output
        ↓
Bit Manipulation
        ↓
CPU Simulation
```

---

# 📊 Practical Status

| Practical | Topic | Status |
|---|---|---|
| P01 | Basic Computer | ✅ Completed |
| P02 | Fetch & Decode | ✅ Completed 
| P03 | Addition | ✅ Completed |
| P04 | Subtraction | ✅ Completed |
| P05 | Logic Operations | ✅ Completed |
| P06 | Memory Reference | ✅ Completed |
| P07 | Register Reference | ✅ Completed |
| P08 | Conditional Skip | ✅ Completed |
| P09 | CIR / CIL | ✅ Completed |
| P10 | Sum Until Negative | ✅ Completed |
| P11 | Sum Until Zero | ✅ Completed |

**Overall Status: P01–P11 Completed 🎉**

---

# 📁 Repository Structure

```text
College/
└── CPU-Sim/
    ├── README.md
    │
    ├── BasicComputer.cpu
    │
    ├── P03_ADD.a
    ├── P04_SUBTRACT.a
    ├── P05_LOGIC.a
    ├── P06_MEMORY_REFERENCE.a
    ├── P07_REGISTER_REF_CLA_CMA_CME_HLT.a
    ├── P08_REGISTER_REF_INC_SPA_SNA_SZE.a
    ├── P09_REGISTER_REF_CIR_CIL.a
    ├── P10_SUM_UNTIL_NEGATIVE.a
    └── P11_SUM_UNTIL_ZERO.a
```

---

# 🛠️ Tools

- **CPU Sim**
- **Mano Basic Computer Architecture**
- **Assembly Language**
- **Git**
- **GitHub**

---

# 🎯 Learning Outcomes

By completing these practicals, the following concepts were studied and practiced:

- CPU organization
- Register organization
- Memory organization
- Instruction format
- Direct and indirect addressing
- Fetch–decode–execute cycle
- Microoperations
- Control signals
- Arithmetic operations
- Two's complement
- Logical operations
- Memory-reference instructions
- Register-reference instructions
- Conditional skip operations
- Branching and loops
- Input/output
- Bit shifting and rotation
- Carry/extend handling
- CPU simulation

---

# 📝 Conclusion

This project provides a practical implementation of the fundamental concepts of **Computer System Architecture** using the **Mano Basic Computer model** and **CPU Sim**.

The practicals progressively demonstrate how CPU registers, memory, instructions, microoperations and control signals work together to execute programs.

---
**Completed**
