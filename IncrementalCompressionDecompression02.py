#!/usr/bin/env python3
import zlib

def main(): 
    #InputData = open('lorem.txt', 'rb').read()
    InputData = b'Hello world'
    
    ##Perfoming CRC Checksum Befor The Compress Alogo
    #cksum = zlib.crc32(InputData)
    #print('CRC-32 : {:12d}'.format(cksum))
    #print(' : {:12d}'.format(zlib.crc32(InputData, cksum)))     
    
    #Initializing Compress Process
    compressed = zlib.compress(InputData , 9)
    combined = compressed
    
    #Initializing Decompressor
    decompressor = zlib.decompressobj()
    decompressed = decompressor.decompress(combined)
    
    ##Matching the Decompressed data with early input
    #decompressed_matches = decompressed == InputData
    #print('Decompressed Matched:', decompressed_matches)  
    
    ##Perfoming CRC Checksum After The Compress Alogo
    #cksum = zlib.crc32(decompressed)
    #print('CRC-32 : {:12d}'.format(cksum))
    #print(' : {:12d}'.format(zlib.crc32(decompressed, cksum)))     
    
    #Get The Decompressed Message 
    decompressedStr = str(decompressed)
    print (decompressedStr)
    decompressedStr = decompressedStr[2:-1]
    print (decompressedStr)

if __name__ == "__main__":
    main()