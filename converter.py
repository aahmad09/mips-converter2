from typing import List
import names
from names import *


def rType(instList: str) -> str:
    bin_shamt = "00000"
    operation = instList[0]
    binOpCode = names.insCodes[operation][0]
    bin_funct = names.insCodes[operation][1]

    if operation in ["sll", "srl"]:
        bin_rd = convertDecToBin(instList[1]).zfill(5)
        bin_rt = convertDecToBin(instList[2]).zfill(5)
        bin_rs = "00000"
        bin_shamt = convertDecToBin(instList[3]).zfill(5)
    elif operation in ["mult", "div", "multu", "divu"]:
        bin_rd = "00000"
        bin_rs = convertDecToBin(instList[1]).zfill(5)
        bin_rt = convertDecToBin(instList[2]).zfill(5)
    elif operation == "jr":
        bin_rs = convertDecToBin(instList[1]).zfill(5)
        bin_rd = "00000"
        bin_rt = "00000"
    elif operation in ["mfhi", "mflo"]:
        bin_rd = convertDecToBin(instList[1]).zfill(5)
        bin_rs = "00000"
        bin_rt = "00000"
    else:  ## operation in ["add", "addu", "sub", "subu", "and"]
        bin_rd = convertDecToBin(instList[1]).zfill(5)
        bin_rs = convertDecToBin(instList[2]).zfill(5)
        bin_rt = convertDecToBin(instList[3]).zfill(5)

    return binOpCode + bin_rs + bin_rt + bin_rd + bin_shamt + bin_funct


def iType(instList: str) -> str:
    operation = instList[0]
    binOpCode = names.insCodes[operation][0]

    if operation in ["beq", "bne"]:
        bin_rs = convertDecToBin(instList[1]).zfill(5)
        bin_rt = convertDecToBin(instList[2]).zfill(5)
        bin_imm = convertDecToBin(instList[3]).zfill(16)
    elif operation in ["lw", "sw"]:
        splittedIns = instList[2].split("(")
        bin_imm = convertDecToBin(splittedIns[0]).zfill(16)
        bin_rs = convertDecToBin(splittedIns[1][:-1]).zfill(5)
        bin_rt = convertDecToBin(instList[1]).zfill(5)
    else:
        bin_rt = convertDecToBin(instList[1]).zfill(5)
        bin_rs = convertDecToBin(instList[2]).zfill(5)

    return binOpCode + bin_rs + bin_rt + bin_imm


def jType(instList: str) -> str:
    operation = instList[0]
    address = instList[1]
    binOpCode = names.insCodes[operation][0].zfill(6)
    binAddress = convertDecToBin(address).zfill(26)
    return binOpCode + binAddress


def convertDecToBin(dec: str) -> str:
    return str(bin(int(dec))[2:])


def convertToRegName(operands: List[str]) -> List[str]:
    if operands[0] in ["lw", "sw"]:
        splittedIns = operands[-1].split("(")
        reg = str(names.registersNames[splittedIns[-1][:-1]])
        lastOperand = splittedIns[0] + "(" + reg + ")"
        return (
            [operands[0]]
            + list(map(lambda x: names.registersNames[x], operands[1:-1]))
            + [lastOperand]
        )
    else:
        return [operands[0]] + list(
            map(lambda x: names.registersNames[x], operands[1:])
        )


def convertMipsToBin(mipsInst: str, regFlags: bool) -> str:
    seperatedInst = mipsInst.split()
    if regFlags:
        seperatedInst = convertToRegName(seperatedInst)
    converted = names.instructionHandler[seperatedInst[0]](seperatedInst)
    return converted


def breakdownBinary(binary):
    op = binary[:6]

    mipsop = getOpBinary(op)
    format = formats.get(mipsop)
    if format == "R":
        rs = binary[6:11]
        rt = binary[11:16]
        rd = binary[16:21]
        shamt = binary[21:26]
        functt = binary[26:32]

        print(op + rs + rt + rd + shamt + functt)

        getop = getFunctBinary(functt)

        getrs = getRegisterBinary(rs)

        getrt = getRegisterBinary(rt)

        getrd = getRegisterBinary(rd)
        holdshamt = int(shamt, 2)
        if holdshamt != 0:
            print(getop + " " + getrs + " " + getrt + " 0x" + str(holdshamt))
        else:
            print(getop + " " + getrd + " " + getrs + " " + getrt)

    elif format == "I":
        rs = binary[6:11]
        rt = binary[11:16]
        immediate = binary[16:32]

        getop = getOpBinary(op)


        getrs = getRegisterBinary(rs)

        getrt = getRegisterBinary(rt)

        getImmediate = immediate
        hexstr = convertImmediate(getImmediate)
        if getop == 'lw' or getop == 'sw':
            print(getop + " " + getrt + " " + "(" + hexstr + ")" + " " + getrs)
        else:
            print(getop + " " + getrt + " " + getrs + " " + hexstr)

    elif format == "J":
        address = binary[6:32]
        getop = getOpBinary(op)
        hexstr = convertImmediate(address)

        print(getop + " " + hexstr)


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


def main():
    ###
    # Uses a while loop to get mips instruction and converts to bin equivalent until the user enters "exit"
    ##
    f = open("guide.txt", "r")
    help_contents = f.read()
    print(help_contents)

    # A boolean to indicate whether to convert binary to mips or mips to binary
    conversionTypeFlag = (
        True
        if input(
            "Do you want to convert mips to binary or binary to mips? Enter 'y' for mips to binary, 'n' for binary to mips: "
        ).lower()
        == "y"
        else False
    )

    # a boolean to indicate whether to use reg names or reg numbers
    regNamesFlag = (
        True
        if input(
            "Do you want to use register names or register numbers? Enter 'y' for register names, 'n' for register numbers: "
        ).lower()
        == "y"
        else False
    )

    if conversionTypeFlag:
        print("-" * 120)
        mipsInst = (
            input("Enter MIPS instruction to be converted: ")
            .lower()
            .replace(",", "")
            .replace("$", "")
        )

        try:
            while mipsInst != "exit":
                print(
                    f"\tConverted instruction in binary:  {convertMipsToBin(mipsInst, regNamesFlag)}"
                )
                print("-" * 120)
                mipsInst = (
                    input("Enter binary MIPS instruction to be converted: ")
                    .lower()
                    .replace(",", "")
                    .replace("$", "")
                )
        except:
            print(
                "\nERROR: Invalid mips instruction format or mips instruction not supported."
            )
    else:
        print("-" * 120)
        binaryInst = input("Enter binary instruction to be converted: ")
        try:
            while binaryInst != "exit":
                breakdownBinary(binaryInst)
                print("-" * 120)
                binaryInst = input("Enter binary instruction to be converted: ")
        except:
            print(
                "\nERROR: Invalid binary instruction format or binary instruction not supported."
            )


if __name__ == "__main__":
    main()
