from typing import Final
import math

BLOCK_SIZE: Final[int] = 8
DECIMAL_TO_BASE92: Final[tuple[str, ...]] = ("!","#","$","%","&","\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~")
BASE92_TO_DECIMAL: Final[dict[str, int]] = {"!":0,"#":1,"$":2,"%":3,"&":4,"'":5,"(":6,")":7,"*":8,"+":9,",":10,"-":11,".":12,"/":13,"0":14,"1":15,"2":16,"3":17,"4":18,"5":19,"6":20,"7":21,"8":22,"9":23,":":24,";":25,"<":26,"=":27,">":28,"?":29,"@":30,"A":31,"B":32,"C":33,"D":34,"E":35,"F":36,"G":37,"H":38,"I":39,"J":40,"K":41,"L":42,"M":43,"N":44,"O":45,"P":46,"Q":47,"R":48,"S":49,"T":50,"U":51,"V":52,"W":53,"X":54,"Y":55,"Z":56,"[":57,"]":58,"^":59,"_":60,"`":61,"a":62,"b":63,"c":64,"d":65,"e":66,"f":67,"g":68,"h":69,"i":70,"j":71,"k":72,"l":73,"m":74,"n":75,"o":76,"p":77,"q":78,"r":79,"s":80,"t":81,"u":82,"v":83,"w":84,"x":85,"y":86,"z":87,"{":88,"|":89,"}":90,"~":91}

def hashset(key: str) -> tuple[int, ...] | bool:
    if len(key) < 1:
        return False
    raw = ""
    sum = 0
    for c in key:
        raw += str(ord(c))
        sum += ord(c)
    scrambled = ""
    for i in range(len(raw)):
        scrambled += str(ord(raw[i]) * sum)
    while len(scrambled) < 8:
        scrambled += scrambled

    return (
        int(scrambled[-1]) % 8,
        int(scrambled[-2]) % 8,
        int(scrambled[-3]) % 8,
        int(scrambled[-4]) % 8,
        int(scrambled[-5]) % 8,
        int(scrambled[-6]) % 8,
        int(scrambled[-7]) % 8,
        int(scrambled[-8]) % 8
    )

def generate_blocks(data: str) -> list[bytearray]:
    blocks: list[bytearray] = []
    raw_bytes = bytearray(data.encode("utf-8"))

    total_blocks = math.ceil(len(raw_bytes) / BLOCK_SIZE)

    for block in range(total_blocks):
        start = block * BLOCK_SIZE
        end = start + BLOCK_SIZE
        blocks.append(raw_bytes[start:end])

    if not blocks:
        blocks.append(bytearray(BLOCK_SIZE))
    else:
        end_pad = BLOCK_SIZE - len(blocks[-1])
        if end_pad == 0:
            blocks.append(bytearray(BLOCK_SIZE))
        else:
            blocks[-1].extend(bytes([end_pad]) * end_pad)

    return blocks

def unpad(data: bytes) -> bytes:
    if not data:
        return b""
    pad_length = data[-1]
    if pad_length == 0:
        return data[:-BLOCK_SIZE]
    else:
        return data[:-pad_length]
    
def slice_blocks(data: bytes) -> list[bytearray]:
    blocks: list[bytearray] = []

    while len(data) > 0:
        blocks.append(bytearray(data[:8]))
        data = data[8:]

    return blocks

def scramble(block: bytearray, hashset: tuple[int, ...]) -> bytearray:
    scrambled = bytearray(8)
    for i in range(BLOCK_SIZE):
        scrambled[i] = block[i] ^ (hashset[i])
    return scrambled

def scramble_blocks(blocks: list[bytearray], fun_numbers: tuple[int, ...]) -> bytes:
    scrambled_blocks: list[bytearray] = []
    
    for i in range(len(blocks)):
        scrambled_blocks.append(scramble(blocks[i], fun_numbers))

    return b"".join(scrambled_blocks)

def decimal_to_base92(decimal: int) -> str | None:
    base_92_string = ""
    if decimal >= 0:
        while True:
            base_92_string = f"{DECIMAL_TO_BASE92[decimal % 92]}{base_92_string}"
            decimal //= 92
            if decimal <= 0:
                break
        return base_92_string
    else:
        return None

def base92_to_decimal(base92: str) -> int:
    decimal = 0
    for c in base92:
        value = BASE92_TO_DECIMAL[c]
        decimal = decimal * 92 + value

    return decimal

def base92_to_bytes(base92: str) -> bytes:
    converted_bytes = bytearray()

    while len(base92) > 0:
        pair = base92[:2]
        base92 = base92[2:]
        base92_number = pair
        if base92_number[0] == "!":
            base92_number = base92_number[1:]
        converted_bytes.append(base92_to_decimal(base92_number))

    return bytes(converted_bytes)

def bytes_to_base92(data: bytes) -> str:
    base92_string = ""
    for byte in data:
        base92_component = decimal_to_base92(byte)
        if base92_component is not None:
            if len(base92_component) == 1:
                base92_string += f"!{base92_component}"
                continue
            base92_string += base92_component

    return base92_string

def encrypt(data: str, key: str) -> str | bool:
    fun_numbers = hashset(key)
    if isinstance(fun_numbers, tuple):
        blocks = generate_blocks(data)
        scrambled_blocks = scramble_blocks(blocks, fun_numbers)
        all_bytes = scrambled_blocks
        base92_string = bytes_to_base92(all_bytes)
        return base92_string
    return False

def decrypt(base92_string: str, key: str) -> str | bool:
    fun_numbers = hashset(key)
    if isinstance(fun_numbers, tuple):
        encrypted_bytes = base92_to_bytes(base92_string)
        sliced_blocks = slice_blocks(encrypted_bytes)
        unscrambled_blocks = scramble_blocks(sliced_blocks, fun_numbers)
        decrypted_data = unscrambled_blocks
        unpadded_data = unpad(decrypted_data)
        original_data = unpadded_data.decode("utf-8")
        return original_data
    return False
