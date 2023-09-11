import string

print('Iban Checker v1.0 (Dont use on actual Ibans this is just a testing script for a iban checker)')
print('Example of a iban. Country; ' + 'PL', 'Checksum; ' + '52', 'Numbers; ' + '5000 1510 0000 23')
print('Without the extra stuff: PL52 5000 1510 0000 23')
while True:
    ibanin1 = input('Insert a country (Shortened version): ')
    if len(ibanin1) > 2:
        print('This is not a shortened version. They are usually 2 characters long!')
        break
    iban2 = input('Insert checksum: ')
    if len(iban2) > 2:
        print('This should be 2 characters long!')
        break
    ibanin2 = input('Insert iban numbers: ')
    N = 4
    ibanin = ibanin1 + iban2 + ibanin2
    output = ibanin.translate({ord(c):  None for c in string.whitespace})
    print('Inserted iban: ',output)
    if len(output) == 18:
        if iban2 in output:
            output[N:]
            xe = output + ibanin1 + iban2
            new = xe.replace(ibanin1,"1518")
            xy = new[6:]
            if (int(xy) % 97) == 1:
                print('Validated:', xy, 'is a real Iban')
                break;
            else:
                print(ibanin, 'Not a real iban try again!')
    else:
        print(ibanin, 'is not a real iban try again!')
