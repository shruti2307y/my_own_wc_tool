#!/usr/bin/env python3
import os;
import argparse
import sys
import signal
def control_c_handler(signal, frame):
    sys.exit(0)
signal.signal(signal.SIGINT, control_c_handler)

def get_bytes(fileContent):
    return str(len(fileContent.encode('utf-8')))
def get_words(fileContent):
    words=fileContent.split()
    return str(len(words))
def get_lines(fileContent):
    count=0
    for line in fileContent.split('\n'):
        count+=1
    # Check for next line char on last line of file
    if len(str(line))==0 :
        count-=1
    return str(count)
def get_characters(fileContent):
    count=0
    for line in fileContent:
        count+=len(line)
    return str(count)
def basename(filePath):
    return os.path.basename(filePath)
def output_console(output,filePath):
    print(f'{output} {basename(filePath)}')

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-c","--bytes",action='store_true',help="Input file name")
    parser.add_argument("-l","--length",action='store_true',help="Input file name")
    parser.add_argument("-w","--words",action='store_true',help="Input file name")
    parser.add_argument("-m","--char",action='store_true',help="Input file name")
    parser.add_argument('file_path', type=str,nargs='?', help='Path to the input file')
    args = parser.parse_args()
    if args.file_path:
        file_path = args.file_path
        with open(file_path, 'r', encoding='utf-8') as file:
            fileContent = file.read()
    else:
        file=sys.stdin
        fileContent = file.read()
        file_path=""


    output=""
    number_bytes=""
    number_char=""
    number_lines=""
    number_words=""
    if(args.bytes):
        number_bytes=get_bytes(fileContent)
        
    if(args.words):
        number_words=get_words(fileContent)
        
    if(args.length):
        number_lines=get_lines(fileContent)
        
    if(args.char):
        number_char=get_characters(fileContent)
    
    if(args.bytes or args.char or args.length or args.words):
        output=f'{number_lines} {number_words} {number_bytes} {number_char}'
    else:
        # If no option is provided, display the default output

        output =f'{get_lines(fileContent)} {get_words(fileContent)} {get_bytes(fileContent)}'
    

    output_console(output,file_path)

if __name__ == "__main__":
    main()