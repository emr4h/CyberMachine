import pefile
import csv

def fileExtract(data):
    print("Extracting the PE information of the file...")
    header =["AddressOfEntryPoint","MajorLinkerVersion","MajorImageVersion","MajorOperatingSystemVersion","DllCharacteristics","SizeOfStackReserve","NumberOfSections","ResourceSize","IfMalware"]
    with open('inputData.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # header bilgilerini ekledik :
        writer.writerow(header)

        # zararlı yazılımların bilgilerini ekledik :
        pe = pefile.PE(data)
        a = str(pe.OPTIONAL_HEADER.AddressOfEntryPoint)
        b = str(pe.OPTIONAL_HEADER.MajorLinkerVersion)
        c = str(pe.OPTIONAL_HEADER.MajorImageVersion)
        d = str(pe.OPTIONAL_HEADER.MajorOperatingSystemVersion)
        e = str(pe.OPTIONAL_HEADER.DllCharacteristics)
        f = str(pe.OPTIONAL_HEADER.SizeOfStackReserve)
        g = str(pe.FILE_HEADER.NumberOfSections)
        h = str(pe.OPTIONAL_HEADER.DATA_DIRECTORY[2].Size)
        i = " " # zararlı bilgisini gösterir.
        inputData = [a,b,c,d,e,f,g,h,i]
        writer.writerow(inputData)
    print("The file was successfully extracted.")

