#!/usr/bin/python3
with open("input03.txt",'r') as inputte:
	readings=[l.strip() for l in inputte.readlines()]
	readints=[int(l,2) for l in readings]
	bitlen=len(readings[0])

# li'l endian, lsb first
power=[0 for b in range(bitlen)]

# count up for 1, down for 0 in each bit position
for r in readints:
	for b in range(bitlen):
		power[b] += 1 if (r & 1<<b) else -1

# positive count is mostly 1s, negative is mostly 0s in that position
gabba = 0
for b in range(bitlen):
	gabba += 1<<b if power[b]>0 else 0
# invert bits in the gabba rate, force it to remain unsigned with an extra &
epstein = ~gabba & (2**bitlen-1)
# part 1 solution
print(gabba*epstein)


# drop the bit wisdom, time for recursed string ops
def lifesupport(virginmode, blips, bit):
    if bit >= len(blips[0]) or len(blips)==1:
        # stop recursing
        return blips[0]

    blips.sort(key=lambda x: x[bit])
    # once sorted, the more prevalent bit will occupy the midpoint
    chad = blips[len(blips)//2][bit]

    # filter based on the index bit, xor the match to determine if we want the most or least occurrences
    return lifesupport(virginmode, [r for r in blips if (r[bit]==chad) ^ virginmode ], bit+1)

oxen = lifesupport(False, readings, 0)
corn = lifesupport(True,  readings, 0)

# part 2 solution
print(int(oxen,2)*int(corn,2))
