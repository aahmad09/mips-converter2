import names


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


def convertMipsToBin(mipsInst: str) -> str:
    seperatedInst = mipsInst.split()
    converted = names.instructionHandler[seperatedInst[0]](seperatedInst)
    return converted


def main():
    ###
    # Uses a while loop to get mips instruction and converts to bin equivalent until the user enters "exit"
    ##
    f = open("guide.txt", "r")
    help_contents = f.read()
    print(help_contents)

    print("-" * 80)
    mipsInst = (
        input("Enter binary MIPS instruction to be converted: ")
        .lower()
        .replace(",", "")
        .replace("$", "")
    )

    try:
        while mipsInst != "exit":
            if mipsInst == "help":
                f = open("help.txt", "r")
                help_contents = f.read()
                print(help_contents)
            print(f"\tConverted instruction in binary:  {convertMipsToBin(mipsInst)}")
            print("-" * 80)
            mipsInst = (
                input("Enter binary MIPS instruction to be converted: ")
                .lower()
                .replace(",", "")
                .replace("$", "")
            )
    except:
        print("ERROR: Invalid instruction format or instruction not supported.")


if __name__ == "__main__":
    main()
