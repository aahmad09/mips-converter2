from converter import rType, iType, jType


insCodes = {
    "add": ("000000", "100000"),  ## R types
    "addu": ("000000", "100001"),
    "sub": ("000000", "100010"),
    "subu": ("000000", "100011"),
    "sll": ("000000", "000000"),
    "srl": ("000000", "000010"),
    "mult": ("000000", "011000"),
    "multu": ("000000", "011001"),
    "div": ("000000", "011010"),
    "divu": ("000000", "011011"),
    "mfhi": ("000000", "010000"),
    "mflo": ("000000", "010010"),
    "jr": ("000000", "001000"),
    "and": ("000000", "100100"),
    "addi": ("001000", "000000"),  ## I types
    "lw": ("100010", "000000"),
    "beq": ("000100", "000000"),
    "bne": ("000101", "000000"),
    "sw": ("101011", "000000"),
    "j": ("000010", "000000"),  ## J types
    "jal": ("000011", "000000"),
}


instructionHandler = {
    "add": rType,
    "addu": rType,
    "sub": rType,
    "subu": rType,
    "sll": rType,
    "srl": rType,
    "mult": rType,
    "multu": rType,
    "div": rType,
    "divu": rType,
    "mfhi": rType,
    "mflo": rType,
    "jr": rType,
    "and": rType,
    "and": rType,
    "addi": iType,
    "lw": iType,
    "beq": iType,
    "bne": iType,
    "sw": iType,
    "j": jType,
    "jal": jType,
}
