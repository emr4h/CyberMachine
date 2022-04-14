
import argparse
import subprocess
import random
from pyfiglet import Figlet
from extractPE import fileExtract
from malwareML import machineLearnMalware
from spamML import machineLearnSpam
from urlML import machineLearnUrl


print("\n\n\n")

fontList = ["big","bulbhead","roman","epic","larry3d","speed","nancyj","stampatello","smslant","slscript","serifcap","rounded","puffy","o8","letters","colossal","basic"]
fontType = random.choice(fontList)
f = Figlet(font=fontType)
print(f.renderText('Cyber Machine'))

print("by emr4h\n")

parser = argparse.ArgumentParser(prog="hackwall\n", description="Threat Analysis Tool for End User", usage="\n\n Malware Analysis with ML:  python3 cybermachine.py --exe <file_path> \n Email Analysis with ML:  python3 cybermachine.py --mail <string> \n Url Analysis with ML: python3 cybermachine.py --url <string>")
parser.add_argument("--exe", help = "Malware Analysis with ML, give value in exe file type")
parser.add_argument("--mail", type=str, help = "Email Spam Analysis with ML, give value in string type ")
parser.add_argument("--url", type=str, help = "Url Spam Analysis with ML, give value in string type ")


args = parser.parse_args() 


def analysisMalware(argument):
    fileExtract(argument)
    result = machineLearnMalware()
    if(result >=2):
        print("ML Prediction --> Malware.\n")
    else:
        print("ML Prediction --> Secure.\n")
    subprocess.call(["rm", "inputData.csv"])


def analysisSpam(argument):
    result = machineLearnSpam(argument)
    if(result >=2):
        print("ML Prediction --> Spam.\n")
    else:
        print("ML Prediction --> Secure.\n")

def analysisUrl(argument):
    result = machineLearnUrl(argument)
    if(result >=2):
        print("ML Prediction --> Spam.\n")
    else:
        print("ML Prediction --> Secure.\n")


if __name__=='__main__':
    
    if(args.exe):
        analysisMalware(args.exe)

    if(args.mail):
        analysisSpam(args.mail)
    
    if(args.url):
        analysisUrl(args.url)

