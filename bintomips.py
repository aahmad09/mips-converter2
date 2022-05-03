def breakdownBinary(binary):
    op = binary[:6]

    mipsop = getOpBinary(op)
    format = formats.get(mipsop)
    if format == 'R':
        rs = binary[6:11]
        rt = binary[11:16]
        rd = binary[16:21]
        shamt = binary[21:26]
        functt = binary[26:32]

        print(op + '\n' + rs + '\n' + rt + '\n' + rd + '\n' + shamt + '\n' + functt)

        getop = getFunctBinary(functt)

        getrs = getRegisterBinary(rs)

        getrt = getRegisterBinary(rt)

        getrd = getRegisterBinary(rd)
        holdshamt = int(shamt, 2)
        if holdshamt != 0:
            print(getop + " " + getrs + " " + getrt + " 0x" + str(holdshamt))
        else:
            print(getop + " " + getrs + " " + getrt + " " + rd)

    elif format == 'I':
        rs = binary[6:11]
        rt = binary[11:16]
        immediate = binary[16:32]

        getop = getOpBinary(op)

        getrs = getRegisterBinary(rs)

        getrt = getRegisterBinary(rt)


        getImmediate = immediate
        hexstr = convertImmediate(getImmediate)


        print(getop + " " + getrt + " " + getrs + " " + hexstr)


    elif format == 'J':
        address = binary[6:32]
        getop = getOpBinary(op)
        hexstr = convertImmediate(address)

        print(getop + " " +  hexstr)

def convertImmediate(binaryr):
    bin = int(binaryr, 2)
    ret = hex(bin)
    return ret

def getRegisterBinary(binaryr):
    return get_key(binaryr, binaryregisters)

def getOpBinary(binaryr):
    return get_key(binaryr, binaryop)

def getFunctBinary(binary):
    return get_key(binary, binaryfunctt)

def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key

binaryregisters = {
    '0': '00000', 'at': '00001', 'v0': '00010', 'v1': '00011',
    'a0': '00100', 'a1': '00101', 'a2': '00110', 'a3': '00111',
    't0': '01000', 't1': '01001', 't2': '01010', 't3': '01011',
    't4': '01100', 't5': '01101', 't6': '01110', 't7': '01111',
    's0': '10000', 's1': '10001', 's2': '10010', 's3': '10011',
    's4': '10100', 's5': '10101', 's6': '10110', 's7': '10111',
    't8': '11000', 't9': '11001', 'k0': '11010', 'k1': '11011',
    'gp': '11100', 'sp': '11101', 'fp': '11110', 'ra': '11111'
}

binaryop = {
    'add' : '000000',
    'addi': '001000', 'addiu': '001001', 'addu' : ['000000', '100001'],
    'and' : ['000000', '100100'], 'andi': '001100', 'beq': '000100', 'bno' : '000101', 'j' : '000010', 'jal' : '000011',
    'jr' : ['000000', '001000'], 'lbu' : '100100', 'lhu' : '100101', 'li' : '110000', 'lui' : '100101', 'lw' : '100011',
    'nor' : ['000000', '100111'], 'or' : ['000000', '100101'], 'ori' : '001101', 'slt' : ['000000', '101010'], 'slti' : '001010',
    'slitu' : '001011', 'sltu' : ['000000', '101011'],  'sll' : ['000000', '000000'], 'srl' : ['000000', '000010'], 'sb' : '101000', 'sc' : '111000'
    , 'sh' : '111001', 'sw' : '101011', 'sub' : ['000000', '100010'], 'subu' : ['000000', '100011']
}

binaryfunctt = {
    'add' : '100000', 'addu' : '100001', 'and' : '100100', 'jr' : '001000', 'or' : '100101', 'slt' : '101010', 'sltu' : '101011', 'sll' : '000000', 'srl' : '000010',
    'sub' : '100010', 'subu' : '100011'
}

formats = {
    'add': 'R',
    'addi': 'I', 'addiu': 'I', 'addu': 'R',
    'and': 'R', 'andi': 'I', 'beq': 'I', 'bne': 'I', 'j': 'J', 'jal': 'J',
    'jr': 'R', 'lbu': 'I', 'lhu': 'I', 'li': 'I', 'lui': 'I', 'lw': 'I',
    'nor': 'R', 'or': 'R', 'ori': 'I', 'slt': 'R', 'slti': 'I',
    'sltiu': 'I', 'sltu': 'R', 'sll' : 'R', 'srl' : 'R', 'sb' : 'I', 'sc' : 'I'
    , 'sh' : 'I', 'sw' : 'I', 'sub' : 'R', 'subu' : 'R'
}




print('00100000000100000000001100100000')
breakdownBinary('00100000000100000000001100100000')

print('')
print('00001100000000000100101000001000')
breakdownBinary('00001100000000000100101000001000')

print('')
print('00000000000010010100000111000000')
breakdownBinary('00000000000010010100000111000000')